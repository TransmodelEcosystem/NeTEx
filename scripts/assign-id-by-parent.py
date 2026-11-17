from lxml import etree
from pathlib import Path
import sys

for file_name in sys.argv[2:]:
    # Bestandspad (pas aan indien nodig)
    input_file = Path(file_name)

    # Namespace map
    ns = {"n": "http://www.netex.org.uk/netex"}

    # Parser met behoud van whitespace
    parser = etree.XMLParser(remove_blank_text=False)
    tree = etree.parse(str(input_file), parser)
    root = tree.getroot()

    # Zoek alle AccessibilityLimitation elementen zonder id
    for elem in root.xpath(f"//n:{sys.argv[1]}[not(@id)]", namespaces=ns):
        parent = elem.getparent()
        if parent is not None:
            if "id" in parent.attrib:
                elem.set("id", parent.attrib["id"])
                elem.set("version", parent.attrib["version"])
            else:
                parent = parent.getparent()
                if parent is not None and "id" in parent.attrib:
                    elem.set("id", parent.attrib["id"])
                    elem.set("version", parent.attrib["version"])




    # Schrijf bestand in-place terug, behoud exacte structuur
    tree.write(str(input_file), encoding="utf-8", xml_declaration=True, pretty_print=False)
