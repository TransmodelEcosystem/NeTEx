import os
from lxml import etree
from collections import defaultdict

XSD_NAMESPACE = "http://www.w3.org/2001/XMLSchema"
NSMAP = {"xsd": XSD_NAMESPACE}

def find_elements_with_dummy_pair(root_dir):
    dummy_elements = defaultdict(list)  # map: base_name -> [(filepath, etree_element)]
    normal_elements = defaultdict(list)

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if not filename.endswith(".xsd"):
                continue
            filepath = os.path.join(dirpath, filename)
            try:
                tree = etree.parse(filepath)
            except Exception as e:
                print(f"Error parsing {filepath}: {e}")
                continue

            for elem in tree.xpath("//xsd:element", namespaces=NSMAP):
                name = elem.get("name")
                if not name:
                    continue
                if name.endswith("_Dummy"):
                    base = name[:-6]
                    dummy_elements[base].append((filepath, elem))
                else:
                    normal_elements[name].append((filepath, elem))

    # Nu zoeken naar matchende paren
    for base in sorted(dummy_elements):
        if base in normal_elements:
            for dummy_file, _ in dummy_elements[base]:
                for normal_file, normal_elem in normal_elements[base]:
                    if normal_elem.get("abstract") == "true":
                        print(f"Pair: {base}_Dummy in {dummy_file}")
                        print(f"      {base}       in {normal_file}")
                        print()

if __name__ == "__main__":
    # Vervang dit pad door jouw projectpad
    find_elements_with_dummy_pair("./xsd")

