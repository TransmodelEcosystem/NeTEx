from lxml import etree
from pathlib import Path
import copy

XSD_ROOT = Path("xsd")
XSD_NS = {"xsd": "http://www.w3.org/2001/XMLSchema"}

def get_version_of_object_ref_attrs(xsd_file: Path):
    """Return all <xsd:attribute> and similar children under VersionOfObjectRefStructure/extension."""
    tree = etree.parse(str(xsd_file))
    ext = tree.xpath(
        "//xsd:complexType[@name='VersionOfObjectRefStructure']/xsd:simpleContent/xsd:extension",
        namespaces=XSD_NS,
    )
    if not ext:
        raise ValueError("VersionOfObjectRefStructure not found or no extension")
    return [copy.deepcopy(c) for c in ext[0] if isinstance(c.tag, str)]

def collect_ref_elements(root_dir: Path):
    """Collect (xsd_file, type_name) for all complexTypes ending with RefStructure."""
    results = []
    for f in root_dir.rglob("*.xsd"):
        if 'xsd/netex' in str(f):
            tree = etree.parse(str(f))
            for ctype in tree.xpath("//xsd:element[substring(@name, string-length(@name) - string-length('Ref') +1) = 'Ref']", namespaces=XSD_NS):
                name = ctype.get("name")
                yield (f, name)

def collect_ref_complextypes(root_dir: Path):
    """Collect (xsd_file, type_name) for all complexTypes ending with RefStructure."""
    results = []
    for f in root_dir.rglob("*.xsd"):
        tree = etree.parse(str(f))
        for ctype in tree.xpath("//xsd:complexType[substring(@name, string-length(@name) - string-length('RefStructure') +1) = 'RefStructure']", namespaces=XSD_NS):
            name = ctype.get("name")
            yield (f, name)

def add_missing_attrs(restriction_elem, version_attrs):
    """Ensure all attributes from VersionOfObjectRefStructure exist, append if missing."""
    existing_names = {a.get("name") for a in restriction_elem.findall("xsd:attribute", XSD_NS)}
    for attr in version_attrs:
        if attr.tag.endswith("attribute"):
            if attr.get("name") not in existing_names:
                restriction_elem.append(copy.deepcopy(attr))

def ensure_nameofrefclass(restriction_elem, type_name: str):
    """Ensure nameOfRefClass attribute exists with correct type and default."""
    existing = restriction_elem.xpath("xsd:attribute[@name='nameOfRefClass']", namespaces=XSD_NS)
    if existing:
        return
    # derive "XXX" from "ScheduledStopPointRefStructure" → "ScheduledStopPoint"
    base = type_name.replace("RefStructure", "")
    attr = etree.Element(f"{{{XSD_NS['xsd']}}}attribute")
    attr.set("name", "nameOfRefClass")
    attr.set("type", f"NameOfClass{base}")
    attr.set("default", base)
    restriction_elem.append(attr)

def process_refstructure_complex_types(xsd_file, version_attrs, valid_ref_classes):
    """Replace extension with restriction for RefStructures that inherit from VersionOfObjectRefStructure."""
    tree = etree.parse(str(xsd_file))
    modified = False

    for ctype in tree.xpath("//xsd:complexType[substring(@name, string-length(@name) - string-length('RefStructure') +1) = 'RefStructure']", namespaces=XSD_NS):
        name = ctype.get("name")
        if name not in valid_ref_classes:
            continue  # skip unrelated RefStructures

        ext = ctype.xpath(".//xsd:extension", namespaces=XSD_NS)
        if not ext:
            continue
        ext_elem = ext[0]
        base = ext_elem.get("base")

        restriction = etree.Element(f"{{{XSD_NS['xsd']}}}restriction", base=base)

        # Kopieer bestaande attributen uit huidige extension
        for child in ext_elem:
            restriction.append(copy.deepcopy(child))

        # Voeg alle ontbrekende attributen van VersionOfObjectRefStructure toe
        add_missing_attrs(restriction, version_attrs)

        # Zorg voor nameOfRefClass
        ensure_nameofrefclass(restriction, name)

        # Vervang in simpleContent
        simple_content = ctype.find("xsd:simpleContent", XSD_NS)
        if simple_content is not None:
            for child in list(simple_content):
                simple_content.remove(child)
            simple_content.append(restriction)
            modified = True

    if modified:
        tree.write(str(xsd_file), encoding="utf-8", xml_declaration=True, pretty_print=True)
    return modified


def has_extension(xsd_file: Path, type_name: str) -> str | None:
    """
    Check if a complexType with given name uses an <xsd:extension>.
    Returns the base type if found, else None.
    """
    tree = etree.parse(str(xsd_file))
    ext = tree.xpath(
        f"//xsd:complexType[@name='{type_name}']//xsd:extension",
        namespaces=XSD_NS
    )
    if ext:
        return ext[0].get("base")
    return None

def main():
    version_attrs = get_version_of_object_ref_attrs(
        XSD_ROOT / "netex_framework/netex_responsibility/netex_relationship_support.xsd"
    )

    # Hier zou jouw analyzer gebruikt worden om te bepalen welke RefStructures erven van VersionOfObjectRefStructure
    # Voorbeeld: valid_ref_classes = {"ScheduledStopPointRefStructure", "StopPlaceRefStructure", ...}
    # → hier voorlopig als placeholder
    from dependencygraph import XSDDependencyAnalyzer  # vervang door jouw echte analyzer
    ref_elements = set(collect_ref_elements(XSD_ROOT))

    analyzer = XSDDependencyAnalyzer()

    analyzer.parse_schemas([XSD_ROOT])
    analyzer.build_dependency_graph()

    all_complex_types = set([])

    for xsd_file, name in ref_elements:
        type_chain = analyzer._get_type_chain(name)
        if "VersionOfObjectRefStructure" not in type_chain:
            continue
        for x in type_chain:
            all_complex_types.add(x)

    for xsd_file, name in collect_ref_complextypes(XSD_ROOT):
        if name in all_complex_types:
            base = has_extension(xsd_file, name)
            if base:
                pass
                # print(f"{xsd_file}: {name} (extends {base})")
            else:
                print(name)

    # Pas enkel de relevante bestanden aan
    # for xsd_file in XSD_ROOT.rglob("*.xsd"):
    #     if not str(xsd_file).startswith("xsd/netex"):
    #         continue
    #    if process_refstructure_complex_types(xsd_file, version_attrs, valid_ref_classes):
    #        print(f"[MODIFIED] {xsd_file}")

if __name__ == "__main__":
    main()

