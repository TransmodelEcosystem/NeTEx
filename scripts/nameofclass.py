import json
import sys
import re

from lxml import etree
from pathlib import Path
from collections import defaultdict


def update_nameofclass_simpletype(schema_file: Path, element_names: list[str]):
    """
    Replace existing <xsd:simpleType name="NameOfClass"> definition with a
    generated one containing enumerations for all element names.
    """
    ns = {"xsd": "http://www.w3.org/2001/XMLSchema"}

    parser = etree.XMLParser(remove_blank_text=False)
    tree = etree.parse(str(schema_file), parser)
    root = tree.getroot()

    existing = root.find(".//xsd:simpleType[@name='NameOfClass']", namespaces=ns)
    if existing is None:
        print(f"⚠️  No NameOfClass found in {schema_file.name}")
        return

    indent = "       "
    newline = "\n"

    new_simple_type = etree.Element(
        "{http://www.w3.org/2001/XMLSchema}simpleType", name="NameOfClass"
    )
    new_simple_type.text = newline + indent

    annotation = etree.SubElement(
        new_simple_type, "{http://www.w3.org/2001/XMLSchema}annotation"
    )
    annotation.text = newline + indent * 2
    doc = etree.SubElement(
        annotation, "{http://www.w3.org/2001/XMLSchema}documentation"
    )
    doc.text = "Type for name of all classes within NeTEx."
    doc.tail = newline + indent
    annotation.tail = newline + indent

    restriction = etree.SubElement(
        new_simple_type,
        "{http://www.w3.org/2001/XMLSchema}restriction",
        base="xsd:Name",
    )
    restriction.text = newline + indent * 2

    for name in element_names:
        enum_el = etree.SubElement(
            restriction, "{http://www.w3.org/2001/XMLSchema}enumeration", value=name
        )
        enum_el.tail = newline + indent * 2

    restriction.tail = newline + indent
    new_simple_type.tail = newline + indent

    # Plaats op zelfde plek als de oude
    parent = existing.getparent()
    parent.replace(existing, new_simple_type)

    tree.write(
        str(schema_file),
        encoding="utf-8",
        xml_declaration=True,
        pretty_print=True,
    )

    print(
        f"✅ Updated NameOfClass in {schema_file.name} ({len(element_names)} enumerations)"
    )


def update_nameofclass_ref_attributes(
    base_dir: Path,
    entity_file: Path,
    entity_dependency_graph: dict[str, list[str]],
    abstract_classes: set[str],
    substitutionGroups: dict[str, set],
    analyzer,
):
    """
    Update all RefStructures across XSD files:
    - Generate or replace NameOfClassXXX simpleTypes in entity_file.
    - Add or replace `nameOfRefClass` attribute in each RefStructure.
    - Supports Variant A: preserves sequences/choices/all/groups; handles simpleContent/complexContent.
    """
    ns = {"xsd": "http://www.w3.org/2001/XMLSchema"}
    parser = etree.XMLParser(remove_blank_text=True)

    # --- Load entity_file (where NameOfClassXXX types will be added) ---
    entity_tree = etree.parse(str(entity_file), parser)
    entity_root = entity_tree.getroot()
    name_of_class_elem = entity_root.find(
        ".//xsd:simpleType[@name='NameOfClass']", namespaces=ns
    )
    if name_of_class_elem is None:
        raise RuntimeError(f"No NameOfClass found in {entity_file.name}")

    complex_todo = set(
        open("scripts/complex-types-included", "r").read().split("\n")
    ) - set(open("scripts/complex-types-excluded", "r").read().split("\n"))
    # print(complex_todo)

    # --- Iterate over all schema files ---
    for schema_file in base_dir.rglob("*.xsd"):
        if "xsd/netex" not in str(schema_file):
            continue

        tree = etree.parse(str(schema_file), parser)
        root = tree.getroot()
        modified = False
        dont = False

        # --- Find all complexTypes ending with RefStructure ---
        for ref_complex in root.findall(".//xsd:complexType", namespaces=ns):
            ref_name = ref_complex.get("name")
            if (
                not ref_name
                or not ref_name.endswith("RefStructure")
                or ref_name not in complex_todo
            ):
                continue

            natural_class = re.sub("RefStructure$", "", ref_name)

            if natural_class in entity_dependency_graph.keys() or (ref_name in ('VehicleEquipmentRefStructure', 'PassengerEquipmentRefStructure')):
                # Determine all concrete descendants
                concrete_classes = [
                    cls
                    for cls in entity_dependency_graph.get(natural_class, [])
                    if cls not in abstract_classes
                ]

                for cls in entity_dependency_graph.get(natural_class + "Ref", []):
                    mycls = re.sub("Ref$", "", cls)
                    if (
                        mycls not in abstract_classes
                        and mycls not in concrete_classes
                        and mycls in entity_dependency_graph.keys()
                        and not mycls.endswith("_Dummy")
                    ):
                        concrete_classes.append(mycls)

                if natural_class not in abstract_classes and natural_class in entity_dependency_graph.keys():
                    concrete_classes.append(natural_class)

                for cls in concrete_classes:
                    if cls in substitutionGroups:
                        for scls in substitutionGroups[cls]:
                            if scls not in abstract_classes and scls in entity_dependency_graph.keys():
                                concrete_classes.append(scls)

                concrete_classes = sorted(set(concrete_classes))
                if not concrete_classes:
                    continue  # nothing to add

                # --- Generate or replace NameOfClassXXX simpleType in entity_file ---
                simple_type_name = f"NameOfClass{ref_name}Type"
                if simple_type_name == "NameOfClassType":
                    simple_type_name = "NameOfClass"
                existing_st = entity_root.find(
                    f".//xsd:simpleType[@name='{simple_type_name}']", namespaces=ns
                )

                new_simple_type = etree.Element(
                    "{http://www.w3.org/2001/XMLSchema}simpleType",
                    name=simple_type_name,
                )
                ann = etree.SubElement(
                    new_simple_type, "{http://www.w3.org/2001/XMLSchema}annotation"
                )
                doc = etree.SubElement(
                    ann, "{http://www.w3.org/2001/XMLSchema}documentation"
                )
                doc.text = f"Type for all concrete EntityStructures that can be referenced from {natural_class}"

                l = analyzer._get_type_chain(natural_class + "Ref")
                if len(l) < 2 or l[1] in (
                    "VersionOfObjectRefStructure",
                    "OrderedVersionOfObjectRefStructure",
                    "ObjectIdType",
                    "normalizedString",
                    "ClassRefStructure",
                    "ObjectIdType",
                    "LinkInSequenceRefStructure",
                    "PointInSequenceRefStructure",
                ):
                    # Workaround
                    parent_ref_name = ""
                elif not l[0].startswith(ref_name) and not l[0].endswith('_InlineType'):
                    parent_ref_name = l[0]

                elif l[1] == ref_name:
                    # Workaround: We don't want circular either.
                    parent_ref_name = l[2]
                    if parent_ref_name.endswith('_Dummy'):
                        parent_ref_name = l[3]
                    if parent_ref_name == 'VersionOfObjectRefStructure':
                        parent_ref_name = ''
                else:
                    parent_ref_name = l[1]
                    if parent_ref_name.endswith('_Dummy'):
                        parent_ref_name = l[2]

                # if parent_ref_name == '':
                #    print(ref_name, l)

                # print(ref_name, parent_ref_name, l)
                # if ref_name == 'LinkRefStructure':
                #    print(ref_name, parent_ref_name, l)
                #    print(natural_class)
                #    print(analyzer._get_type_chain(natural_class + "Ref"))
                #    raise

                if parent_ref_name == '':
                    base = "NameOfClass"
                else:
                    base = f"NameOfClass{parent_ref_name}Type"

                restriction = etree.SubElement(
                    new_simple_type,
                    "{http://www.w3.org/2001/XMLSchema}restriction",
                    base=base,
                )
                for cls in concrete_classes:
                    etree.SubElement(
                        restriction,
                        "{http://www.w3.org/2001/XMLSchema}enumeration",
                        value=cls,
                    )

                if existing_st is not None:
                    parent = existing_st.getparent()
                    parent.replace(existing_st, new_simple_type)
                else:
                    idx = list(entity_root).index(name_of_class_elem)
                    entity_root.insert(idx + 1, new_simple_type)

                # --- Determine where to place the attribute ---
                # Variant A: if there are child elements (sequence/choice/all/group), place directly in complexType
                child_container = None
                for tag in ("sequence", "choice", "all", "group"):
                    child_container = ref_complex.find(
                        f"{{http://www.w3.org/2001/XMLSchema}}{tag}"
                    )
                    if child_container is not None:
                        break

                if child_container is not None:
                    # Place attribute directly in complexType
                    parent_for_attr = ref_complex
                else:
                    # Search for existing simpleContent or complexContent + extension/restriction
                    parent_for_attr = None
                    for tag in ("simpleContent", "complexContent"):
                        elem = ref_complex.find(
                            f"{{http://www.w3.org/2001/XMLSchema}}{tag}"
                        )
                        if elem is not None:
                            # take the first child (extension or restriction)
                            child = next(
                                (
                                    c
                                    for c in elem
                                    if etree.QName(c).localname
                                    in ("extension", "restriction")
                                ),
                                None,
                            )
                            if child is not None:
                                if etree.QName(child).localname == "extension":
                                    print(f"WARNING: extension found in {ref_complex}")
                                    dont = True

                                parent_for_attr = child
                                break
                            else:
                                # If simpleContent exists but no extension/restriction → create restriction
                                parent_for_attr = etree.SubElement(
                                    elem,
                                    "{http://www.w3.org/2001/XMLSchema}restriction",
                                    base="xsd:string",
                                )
                                break
                    # If still None, create new simpleContent/restriction
                    if parent_for_attr is None:
                        elem = etree.SubElement(
                            ref_complex,
                            "{http://www.w3.org/2001/XMLSchema}simpleContent",
                        )
                        parent_for_attr = etree.SubElement(
                            elem,
                            "{http://www.w3.org/2001/XMLSchema}restriction",
                            base="xsd:string",
                        )

                attrib = etree.Element(
                    "{http://www.w3.org/2001/XMLSchema}attribute",
                    name="nameOfRefClass",
                    type=simple_type_name,
                )
                if natural_class in abstract_classes or natural_class not in entity_dependency_graph.keys():
                    # attrib.attrib["use"] = "required"
                    pass
                else:
                    attrib.attrib["default"] = natural_class

                ann = etree.SubElement(
                    attrib, "{http://www.w3.org/2001/XMLSchema}annotation"
                )
                doc = etree.SubElement(
                    ann, "{http://www.w3.org/2001/XMLSchema}documentation"
                )
                doc.text = f"Automatic reference class for {ref_name}"

                # --- Add or replace nameOfRefClass attribute ---
                existing_attr = parent_for_attr.find(
                    "{http://www.w3.org/2001/XMLSchema}attribute[@name='nameOfRefClass']"
                )
                if existing_attr is not None:
                    index = parent_for_attr.index(existing_attr)
                    parent_for_attr.remove(existing_attr)
                    parent_for_attr.insert(index, attrib)
                else:
                    parent_for_attr.append(attrib)

                modified = True
            else:
                print(f"WARNING: {ref_name} has an unknown {natural_class}. Skipping")

        # --- Write file if modified ---
        if modified and not dont:
            str(schema_file),
            tree.write(
                str(schema_file),
                encoding="utf-8",
                xml_declaration=True,
                pretty_print=True,
            )
            print(f"🔧 Updated RefStructures in {schema_file.name}")

    # --- Write back entity_file with updated NameOfClassXXX ---
    entity_tree.write(
        str(entity_file),
        encoding="utf-8",
        xml_declaration=True,
        pretty_print=True,
    )
    print(f"✅ Updated NameOfClassXXX simpleTypes in {entity_file.name}")


if __name__ == "__main__":
    from dependencygraph import XSDDependencyAnalyzer

    base_dir = Path(sys.argv[1])
    target_namespace = "http://www.netex.org.uk/netex"  # pas aan indien nodig
    schema_with_nameofclass = (
        base_dir / "netex_framework/netex_responsibility/netex_entity_support.xsd"
    )

    # Bouw dependency graph + abstract classes
    analyzer = XSDDependencyAnalyzer()
    analyzer.parse_schemas([base_dir])
    analyzer.build_dependency_graph()
    entity_dependency_graph = analyzer.get_simple_graph(None)
    abstract_classes = analyzer.abstract_elements

    # NameOfClass vervangen
    interesting_classes = set(
        [
            x
            for x in entity_dependency_graph.keys()
            if not x.endswith("_Dummy") and not x.endswith("_DummyType")
        ]
    )
    update_nameofclass_simpletype(
        schema_with_nameofclass, sorted(list(interesting_classes) + ['gml:Polygon', 'gml:MultiPolygon', 'gml:MultiSurface', 'gml:pos', 'gml:LineString'])
    )

    # Update RefStructure types + nameOfRefClass attribuut
    update_nameofclass_ref_attributes(
        base_dir,
        schema_with_nameofclass,
        entity_dependency_graph,
        abstract_classes,
        analyzer.substitutionGroups,
        analyzer,
    )
