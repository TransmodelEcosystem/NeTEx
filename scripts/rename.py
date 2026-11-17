import glob
from lxml import etree

XSD_NS = "http://www.w3.org/2001/XMLSchema"
NSMAP = {"xs": XSD_NS}

# Attributen met één enkele type-ref
SINGLE_REF_ATTRS = {'type', 'base', 'ref', 'substitutionGroup', 'itemType'}

# Attributen met meerdere type-refs (spatiegescheiden)
MULTI_REF_ATTRS = {'memberTypes'}

def collect_renames(xsd_files):
    rename_map = {}
    for file in xsd_files:
        tree = etree.parse(file)
        for tag in ['xs:element', 'xs:complexType', 'xs:simpleType']:
            for elem in tree.xpath(f'//{tag}', namespaces=NSMAP):
                name = elem.get("name")
                if name and name.endswith("_"):
                    rename_map[name] = name + "Dummy"
                # if name and name.endswith("_DummyTypeAbstract"):
                #     rename_map[name] = name.replace('_DummyTypeAbstract', "_Abstract")
    return rename_map

def apply_renames(xsd_files, rename_map):
    for file in xsd_files:
        tree = etree.parse(file)
        root = tree.getroot()
        changed = False

        for elem in root.iter():
            # Pas name aan
            if "name" in elem.attrib:
                old = elem.attrib["name"]
                if old in rename_map:
                    elem.attrib["name"] = rename_map[old]
                    changed = True

            # Pas enkelvoudige verwijzingen aan
            for attr in SINGLE_REF_ATTRS:
                if attr in elem.attrib:
                    value = elem.attrib[attr]
                    if ":" not in value and value in rename_map:
                        elem.attrib[attr] = rename_map[value]
                        changed = True

            # Pas meervoudige verwijzingen aan (zoals bij xs:union)
            for attr in MULTI_REF_ATTRS:
                if attr in elem.attrib:
                    values = elem.attrib[attr].split()
                    new_values = [
                        rename_map.get(v, v) if ':' not in v else v
                        for v in values
                    ]
                    if new_values != values:
                        elem.attrib[attr] = ' '.join(new_values)
                        changed = True

        if changed:
            print(f"Updated {file}")
            tree.write(file, encoding="utf-8", xml_declaration=True, pretty_print=True)

def main():
    xsd_files = glob.glob("xsd/**/*.xsd", recursive=True)
    rename_map = collect_renames(xsd_files)
    if not rename_map:
        print("Geen hernoemingen nodig.")
        return
    print("Te hernoemen:", rename_map)
    apply_renames(xsd_files, rename_map)

if __name__ == "__main__":
    main()
