"""
Namespaced XSD Schema Dependency Analyzer
Properly tracks elements and types with namespaces, builds complete dependency graphs,
and provides queryable in-memory interface.
"""

# TODO implement the sub elements originating from groups

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, Set, List, Tuple, Optional, Any
from dataclasses import dataclass, field
from collections import defaultdict
import json


# Type alias for namespaced identifiers
QName = Tuple[str, str]  # (namespace, local_name)


@dataclass
class AttributeDef:
    """Represents an attribute declaration on a complex type."""
    name: str
    type_ref: Optional[QName] = None
    use: str = "optional"  # 'required' or 'optional'
    default: Optional[str] = None
    fixed: Optional[str] = None
    defined_in: Optional[QName] = None  # the complexType qname where this attribute is declared


@dataclass
class SubElementDef:
    """Represents a local element declaration inside a complex type."""
    name: str
    type_ref: Optional[QName] = None
    min_occurs: Optional[str] = None
    max_occurs: Optional[str] = None
    defined_in: Optional[QName] = None


@dataclass
class ComplexType:
    """Represents a complex type definition."""
    namespace: str
    name: str
    base_type: Optional[QName] = None
    derivation_method: Optional[str] = None  # 'extension' or 'restriction'
    attributes: Dict[str, AttributeDef] = field(default_factory=dict)
    subelements: Dict[str, SubElementDef] = field(default_factory=dict)

    def qname(self) -> QName:
        return (self.namespace, self.name)


@dataclass
class Element:
    """Represents a top-level element definition."""
    namespace: str
    name: str
    type_ref: Optional[QName] = None
    is_abstract: bool = False
    substitution_group: Optional[QName] = None

    def qname(self) -> QName:
        return (self.namespace, self.name)


class XSDSchemaAnalyzer:
    """
    Analyzes XSD schemas with proper namespace handling.
    Provides queryable interface for dependency analysis.
    """

    XSD_NS = "http://www.w3.org/2001/XMLSchema"

    def __init__(self):
        # Core storage
        self.elements: Dict[QName, Element] = {}
        self.complex_types: Dict[QName, ComplexType] = {}

        # Namespace prefix mappings per file (for resolution)
        self.ns_prefixes: Dict[str, Dict[str, str]] = {}  # filepath -> {prefix: uri}

        # Computed relationships (built after parsing)
        self._type_descendants: Dict[QName, Set[QName]] = defaultdict(set)
        self._type_ancestors: Dict[QName, List[QName]] = {}
        self._element_descendants: Dict[QName, Set[QName]] = defaultdict(set)
        self._element_ancestors: Dict[QName, List[QName]] = {}
        self._substitution_members: Dict[QName, Set[QName]] = defaultdict(set)

        self._built = False

    def parse_schemas(self, schema_paths: List[Path]) -> None:
        """Parse all XSD schemas from the given paths."""
        for path in schema_paths:
            if path.is_file():
                self._parse_schema_file(path)
            elif path.is_dir():
                for xsd_file in path.rglob("*.xsd"):
                    if 'xsd/netex' in str(xsd_file) or 'xsd/gml' in str(xsd_file):
                        self._parse_schema_file(xsd_file)

        print(f"Parsed {len(self.elements)} elements and {len(self.complex_types)} complex types")

    def _parse_schema_file(self, filepath: Path) -> None:
        """Parse a single XSD schema file."""
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()

            # Extract namespace mappings from root element
            ns_map = self._extract_namespace_map(root)
            self.ns_prefixes[str(filepath)] = ns_map

            # Get target namespace
            target_ns = root.get('targetNamespace', '')
            target_prefix = self._get_prefix_for_namespace(ns_map, target_ns)

            if not target_prefix:
                print(f"Warning: No target namespace prefix found in {filepath}")
                return

            # Parse complex types
            self._extract_complex_types(root, target_prefix, ns_map)

            # Parse elements
            self._extract_elements(root, target_prefix, ns_map)

        except Exception as e:
            print(f"Error parsing {filepath}: {e}")

    def _extract_namespace_map(self, root: ET.Element) -> Dict[str, str]:
        """Extract namespace prefix to URI mappings from schema root."""
        # Note: for your NetEx files we previously used a fixed map; keep it but try to extract real mappings if present.
        ns_map = {'gml': 'http://www.opengis.net/gml/3.2', 'netex': 'http://www.netex.org.uk/netex', 'siri': 'http://www.siri.org.uk/siri' }

        # Try to read declared xmlns attributes (ElementTree stores them in root.attrib with full names)
        # For safety keep the default entries above and only override if discovered.
        for attr_name, attr_value in root.attrib.items():
            if attr_name == 'xmlns':
                ns_map[''] = attr_value
            elif attr_name.startswith('xmlns:'):
                prefix = attr_name.split(':', 1)[1]
                ns_map[prefix] = attr_value

        # Also try to capture default namespace using tag
        if root.tag.startswith('{'):
            default_ns = root.tag.split('}')[0].strip('{')
            if default_ns:
                # Only set default if it's not already present as a known prefix
                ns_map.setdefault('', default_ns)

        return ns_map

    def _get_prefix_for_namespace(self, ns_map: Dict[str, str], namespace: str) -> Optional[str]:
        """Get the prefix for a given namespace URI."""
        for prefix, uri in ns_map.items():
            if uri == namespace:
                # Prefer named prefixes over default namespace
                if prefix:
                    return prefix

        # If no named prefix found, check if it's the default namespace
        for prefix, uri in ns_map.items():
            if uri == namespace:
                return prefix if prefix else 'default'

        return None

    def _resolve_qname(self, qname_str: str, ns_map: Dict[str, str], target_prefix: str) -> Optional[QName]:
        """
        Resolve a QName string to (namespace_prefix, local_name).
        Returns None if the QName is a built-in XSD type.
        """
        if not qname_str:
            return None

        if ':' in qname_str:
            prefix, local_name = qname_str.split(':', 1)
            # Skip XSD built-in types
            if prefix in ('xs', 'xsd'):
                return None
            return (prefix, local_name)
        else:
            # No prefix means target namespace
            return (target_prefix, qname_str)

    def _parse_attributes_from_element(self, xml_elem: ET.Element, ns_map: Dict[str, str], target_prefix: str, defined_in_qname: QName) -> Dict[str, AttributeDef]:
        """
        Parse xsd:attribute nodes under xml_elem (not global attribute refs).
        Returns dict name -> AttributeDef (per this defining complex type).
        """
        attrs: Dict[str, AttributeDef] = {}
        for attr_el in xml_elem.findall(f".//{{{self.XSD_NS}}}attribute"):
            # Support both 'name' and 'ref'
            name = attr_el.get('name')
            ref = attr_el.get('ref')
            if ref and not name:
                # If it's a reference to a global attribute, resolve name from ref
                resolved = self._resolve_qname(ref, ns_map, target_prefix)
                if resolved:
                    name = resolved[1]
                else:
                    # Built-in or unresolved; take local part
                    name = ref.split(':')[-1]

            if not name:
                continue

            # type can be specified or inherited via ref (we don't resolve global attribute definitions)
            type_str = attr_el.get('type', '')
            type_ref = self._resolve_qname(type_str, ns_map, target_prefix) if type_str else None

            use = attr_el.get('use', 'optional')
            default = attr_el.get('default')
            fixed = attr_el.get('fixed')

            attr_def = AttributeDef(
                name=name,
                type_ref=type_ref,
                use=use,
                default=default,
                fixed=fixed,
                defined_in=defined_in_qname
            )

            attrs[name] = attr_def

        return attrs


    def _parse_subelements_from_element(self, xml_elem: ET.Element, ns_map: Dict[str, str],
                                        target_prefix: str, defined_in_qname: QName) -> Dict[str, SubElementDef]:
        subs: Dict[str, SubElementDef] = {}
        for sub_el in xml_elem.findall(f".//{{{self.XSD_NS}}}element"):
            name = sub_el.get('name')
            if not name:
                continue
            if name == 'ServiceJourneyPatternType':
                print(name)
            type_str = sub_el.get('type', '')
            type_ref = self._resolve_qname(type_str, ns_map, target_prefix) if type_str else None
            sub_def = SubElementDef(
                name=name,
                type_ref=type_ref,
                min_occurs=sub_el.get('minOccurs'),
                max_occurs=sub_el.get('maxOccurs'),
                defined_in=defined_in_qname
            )
            subs[name] = sub_def
        return subs


    def _extract_complex_types(self, root: ET.Element, target_prefix: str, ns_map: Dict[str, str]) -> None:
        """Extract all complex type definitions."""
        for ctype in root.findall(f".//{{{self.XSD_NS}}}complexType"):
            name = ctype.get('name')
            if not name:
                continue

            base_type = None
            derivation_method = None

            # Check for extension
            extension = ctype.find(f".//{{{self.XSD_NS}}}extension")
            if extension is not None:
                base_str = extension.get('base', '')
                base_type = self._resolve_qname(base_str, ns_map, target_prefix)
                derivation_method = 'extension'

            # Check for restriction
            restriction = ctype.find(f".//{{{self.XSD_NS}}}restriction")
            if restriction is not None:
                base_str = restriction.get('base', '')
                base_type = self._resolve_qname(base_str, ns_map, target_prefix)
                derivation_method = 'restriction'

            complex_type = ComplexType(
                namespace=target_prefix,
                name=name,
                base_type=base_type,
                derivation_method=derivation_method
            )

            # Parse attributes declared in this complexType (including those inside extension/restriction blocks)
            defined_in_qname = complex_type.qname()
            parsed_attrs = self._parse_attributes_from_element(ctype, ns_map, target_prefix, defined_in_qname)
            complex_type.attributes.update(parsed_attrs)

            parsed_subelements = self._parse_subelements_from_element(ctype, ns_map, target_prefix, defined_in_qname)
            complex_type.subelements.update(parsed_subelements)

            self.complex_types[complex_type.qname()] = complex_type

    def _extract_elements(self, root: ET.Element, target_prefix: str, ns_map: Dict[str, str]) -> None:
        """Extract all element definitions."""
        for elem in root.findall(f"./{{{self.XSD_NS}}}element"):
            name = elem.get('name')
            if not name:
                continue

            # Type reference
            type_str = elem.get('type', '')
            type_ref = self._resolve_qname(type_str, ns_map, target_prefix) if type_str else None

            # Abstract attribute
            is_abstract = elem.get('abstract', 'false').lower() == 'true'

            # Substitution group
            subst_str = elem.get('substitutionGroup', '')
            substitution_group = self._resolve_qname(subst_str, ns_map, target_prefix) if subst_str else None

            # Handle inline complex types
            inline_ctype = elem.find(f"{{{self.XSD_NS}}}complexType")
            if inline_ctype is not None and not type_ref:
                # Create synthetic type name
                inline_name = f"{name}_InlineType"
                inline_qname = (target_prefix, inline_name)

                base_type = None
                derivation_method = None

                restriction = inline_ctype.find(f".//{{{self.XSD_NS}}}restriction")
                extension = inline_ctype.find(f".//{{{self.XSD_NS}}}extension")

                if restriction is not None:
                    base_str = restriction.get('base', '')
                    base_type = self._resolve_qname(base_str, ns_map, target_prefix)
                    derivation_method = 'restriction'
                elif extension is not None:
                    base_str = extension.get('base', '')
                    base_type = self._resolve_qname(base_str, ns_map, target_prefix)
                    derivation_method = 'extension'

                if base_type:
                    inline_type = ComplexType(
                        namespace=target_prefix,
                        name=inline_name,
                        base_type=base_type,
                        derivation_method=derivation_method
                    )
                    # Parse attributes on the inline complexType
                    parsed_attrs = self._parse_attributes_from_element(inline_ctype, ns_map, target_prefix, inline_qname)
                    inline_type.attributes.update(parsed_attrs)

                    self.complex_types[inline_qname] = inline_type
                    type_ref = inline_qname

            element = Element(
                namespace=target_prefix,
                name=name,
                type_ref=type_ref,
                is_abstract=is_abstract,
                substitution_group=substitution_group
            )

            self.elements[element.qname()] = element

    def build_relationships(self) -> None:
        """Build all dependency and inheritance relationships."""
        print("Building relationships...")

        # Build type hierarchy relationships
        self._build_type_hierarchy()

        # Build element hierarchy relationships
        self._build_element_hierarchy()

        # Build substitution group relationships
        self._build_substitution_groups()

        self._built = True
        print("Relationships built successfully")

    def _build_type_hierarchy(self) -> None:
        """Build ancestor and descendant relationships for types."""
        # Build ancestors (going up the hierarchy)
        for qname, ctype in self.complex_types.items():
            ancestors = []
            current = ctype.base_type

            while current and current in self.complex_types:
                ancestors.append(current)
                current = self.complex_types[current].base_type

            self._type_ancestors[qname] = ancestors

        # Build descendants (going down the hierarchy)
        for qname, ctype in self.complex_types.items():
            if ctype.base_type:
                self._type_descendants[ctype.base_type].add(qname)

        # Make descendants transitive
        self._type_descendants = self._compute_transitive_descendants(self._type_descendants)

    def _build_element_hierarchy(self) -> None:
        """Build ancestor and descendant relationships for elements through their types."""
        # Build ancestors for elements
        for elem_qname, element in self.elements.items():
            ancestors = []

            if element.type_ref and element.type_ref in self.complex_types:
                # Follow the type hierarchy
                type_ancestors = self._type_ancestors.get(element.type_ref, [])

                # Find elements that use these ancestor types
                for ancestor_type in type_ancestors:
                    for other_qname, other_elem in self.elements.items():
                        if other_elem.type_ref == ancestor_type:
                            # Check if this type is "specific" to that element
                            if self._is_element_specific_type(other_qname, ancestor_type):
                                ancestors.append(other_qname)
                                break

            self._element_ancestors[elem_qname] = ancestors

        # Build descendants for elements
        for elem_qname, element in self.elements.items():
            if not element.type_ref:
                continue

            # Get all types that descend from this element's type
            if element.type_ref in self._type_descendants:
                descendant_types = self._type_descendants[element.type_ref]

                # Find elements that use these descendant types
                for other_qname, other_elem in self.elements.items():
                    if other_elem.type_ref in descendant_types:
                        # Check if the element's type name contains the element name
                        if self._is_element_specific_type(other_qname, other_elem.type_ref):
                            self._element_descendants[elem_qname].add(other_qname)

    def _is_element_specific_type(self, elem_qname: QName, type_qname: QName) -> bool:
        """Check if a type is specific to an element (contains element name in type name)."""
        elem_name = elem_qname[1]
        type_name = type_qname[1]
        return elem_name in type_name

    def _build_substitution_groups(self) -> None:
        """Build substitution group relationships (recursive)."""
        # Direct substitution relationships
        direct_subst = defaultdict(set)
        for elem_qname, element in self.elements.items():
            if element.substitution_group:
                direct_subst[element.substitution_group].add(elem_qname)

        # Make it transitive: if B substitutes A, and C substitutes B, then C also substitutes A
        self._substitution_members = self._compute_transitive_descendants(direct_subst)

    def _compute_transitive_descendants(self, direct_deps: Dict[QName, Set[QName]]) -> Dict[QName, Set[QName]]:
        """Compute transitive closure of descendant relationships."""
        result = defaultdict(set)

        # Start with direct relationships
        for parent, children in direct_deps.items():
            result[parent] = set(children)

        # Add transitive relationships
        changed = True
        while changed:
            changed = False
            for parent in list(result.keys()):
                current_children = set(result[parent])
                for child in current_children:
                    if child in result:
                        for grandchild in result[child]:
                            if grandchild not in result[parent]:
                                result[parent].add(grandchild)
                                changed = True

        return result

    # New helper: format qname to readable string
    def _qname_to_str(self, qn: Optional[QName]) -> Optional[str]:
        if qn is None:
            return None
        return f"{qn[0]}:{qn[1]}"

    # New public API: combined attributes following inheritance rules
    def get_combined_attributes(self, type_qname: QName) -> List[Dict[str, Any]]:
        """
        Return the combined attributes for the given complex type, following XSD inheritance rules.
        - Attributes from base types are included first.
        - If derived types redeclare an attribute with the same name, the derived declaration replaces
          the base declaration (the properties: type/use/default/fixed come from the most derived).
        - The returned list preserves the initial order of first encounter (base-first).
        Each entry is a dict with keys: name, type, use, default, fixed, defined_in
        """
        if type_qname not in self.complex_types:
            raise KeyError(f"Type {type_qname} not found in complex_types")

        # Build ancestor chain root-first -> immediate parent -> type itself
        # If relationships built, use them; otherwise compute on the fly
        if self._built:
            ancestors = self.get_type_ancestor_chain(type_qname)  # immediate parent -> root
            chain = list(reversed(ancestors))  # root -> immediate parent
            chain.append(type_qname)
        else:
            # Walk base_type pointers to collect chain
            chain = []
            stack = []
            current = self.complex_types[type_qname].base_type
            while current and current in self.complex_types:
                stack.append(current)
                current = self.complex_types[current].base_type
            chain = list(reversed(stack))
            chain.append(type_qname)

        combined: Dict[str, AttributeDef] = {}
        order: List[str] = []

        for t_qn in chain:
            ctype = self.complex_types.get(t_qn)
            if not ctype:
                continue
            # attributes declared in this specific type
            for attr_name, attr_def in ctype.attributes.items():
                if attr_name not in combined:
                    # first encounter -> record and preserve insertion order
                    combined[attr_name] = AttributeDef(
                        name=attr_def.name,
                        type_ref=attr_def.type_ref,
                        use=attr_def.use,
                        default=attr_def.default,
                        fixed=attr_def.fixed,
                        defined_in=attr_def.defined_in
                    )
                    order.append(attr_name)
                else:
                    # overridden/redeclared in derived type: update properties but keep order position
                    existing = combined[attr_name]
                    existing.type_ref = attr_def.type_ref
                    existing.use = attr_def.use
                    existing.default = attr_def.default
                    existing.fixed = attr_def.fixed
                    existing.defined_in = attr_def.defined_in

        # Build output list in preserved order
        result: List[Dict[str, Any]] = []
        for name in order:
            ad = combined[name]
            result.append({
                'name': ad.name,
                'type': self._qname_to_str(ad.type_ref),
                'use': ad.use,
                'default': ad.default,
                'fixed': ad.fixed,
                'defined_in': self._qname_to_str(ad.defined_in)
            })

        return result

    # Query API

    def get_element(self, qname: QName) -> Optional[Element]:
        """Get an element by its qualified name."""
        return self.elements.get(qname)

    def get_complex_type(self, qname: QName) -> Optional[ComplexType]:
        """Get a complex type by its qualified name."""
        return self.complex_types.get(qname)

    def is_abstract(self, element_qname: QName) -> bool:
        """Check if an element is abstract."""
        element = self.elements.get(element_qname)
        return element.is_abstract if element else False

    def get_ancestor_chain(self, element_qname: QName) -> List[QName]:
        """
        Get the complete ancestor chain for an element (what it builds upon).
        Returns list from immediate parent to root.
        """
        if not self._built:
            raise RuntimeError("Call build_relationships() first")

        return self._element_ancestors.get(element_qname, [])

    def get_all_descendants(self, element_qname: QName) -> Set[QName]:
        """
        Get all elements that build upon this element (descendants).
        """
        if not self._built:
            raise RuntimeError("Call build_relationships() first")

        return self._element_descendants.get(element_qname, set())

    def get_substitution_group_members(self, element_qname: QName) -> Set[QName]:
        """
        Get all elements that can substitute for this element (recursive).
        """
        if not self._built:
            raise RuntimeError("Call build_relationships() first")

        return self._substitution_members.get(element_qname, set())

    def get_implementations(self, abstract_element_qname: QName) -> Set[QName]:
        """
        Get all concrete elements that implement an abstract element.
        This includes:
        1. Elements in its substitution group
        2. Elements whose types extend this element's type
        """
        if not self._built:
            raise RuntimeError("Call build_relationships() first")

        implementations = set()

        # Add substitution group members
        implementations.update(self._substitution_members.get(abstract_element_qname, set()))

        # Add type-based descendants
        implementations.update(self._element_descendants.get(abstract_element_qname, set()))

        # Filter out abstract elements
        return {qname for qname in implementations if not self.is_abstract(qname)}

    def get_type_ancestor_chain(self, type_qname: QName) -> List[QName]:
        """Get the complete ancestor chain for a type."""
        if not self._built:
            raise RuntimeError("Call build_relationships() first")

        return self._type_ancestors.get(type_qname, [])

    def get_type_descendants(self, type_qname: QName) -> Set[QName]:
        """Get all types that descend from this type."""
        if not self._built:
            raise RuntimeError("Call build_relationships() first")

        return self._type_descendants.get(type_qname, set())

    def get_all_elements(self) -> Dict[QName, Element]:
        """Get all elements."""
        return self.elements

    def get_all_types(self) -> Dict[QName, ComplexType]:
        """Get all complex types."""
        return self.complex_types

    def get_abstract_elements(self) -> Set[QName]:
        """Get all abstract elements."""
        return {qname for qname, elem in self.elements.items() if elem.is_abstract}

    # Export functions

    def export_to_json(self, output_path: Path) -> None:
        """Export complete analysis to JSON."""
        if not self._built:
            raise RuntimeError("Call build_relationships() first")

        result = {
            'elements': {},
            'types': {},
            'abstract_elements': [self._qname_to_str(qn) for qn in self.get_abstract_elements()]
        }

        # Export elements
        for qname, element in self.elements.items():
            qname_str = self._qname_to_str(qname)
            result['elements'][qname_str] = {
                'namespace': element.namespace,
                'name': element.name,
                'type': self._qname_to_str(element.type_ref) if element.type_ref else None,
                'is_abstract': element.is_abstract,
                'substitution_group': self._qname_to_str(element.substitution_group) if element.substitution_group else None,
                'ancestors': [self._qname_to_str(a) for a in self.get_ancestor_chain(qname)],
                'descendants': [self._qname_to_str(d) for d in sorted(self.get_all_descendants(qname))],
                'substitution_members': [self._qname_to_str(s) for s in sorted(self.get_substitution_group_members(qname))],
            }

            if element.is_abstract:
                result['elements'][qname_str]['implementations'] = [
                    self._qname_to_str(i) for i in sorted(self.get_implementations(qname))
                ]

        # Export types
        for qname, ctype in self.complex_types.items():
            qname_str = self._qname_to_str(qname)
            result['types'][qname_str] = {
                'namespace': ctype.namespace,
                'name': ctype.name,
                'base_type': self._qname_to_str(ctype.base_type) if ctype.base_type else None,
                'derivation_method': ctype.derivation_method,
                'ancestors': [self._qname_to_str(a) for a in self.get_type_ancestor_chain(qname)],
                'descendants': [self._qname_to_str(d) for d in sorted(self.get_type_descendants(qname))],
                'attributes': {
                    aname: {
                        'type': self._qname_to_str(adef.type_ref),
                        'use': adef.use,
                        'default': adef.default,
                        'fixed': adef.fixed,
                        'defined_in': self._qname_to_str(adef.defined_in)
                    } for aname, adef in ctype.attributes.items()
                },
                'subelements': {
                    sname: {
                        'type': self._qname_to_str(sdef.type_ref),
                        'min_occurs': sdef.min_occurs,
                        'max_occurs': sdef.max_occurs,
                        'defined_in': self._qname_to_str(sdef.defined_in)
                    } for sname, sdef in ctype.subelements.items()
                }
            }

        with open(output_path, 'w') as f:
            json.dump(result, f, indent=2)

        print(f"\nExported complete analysis to: {output_path}")


def main():
    """Example usage."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python xsd_analyzer_v2.py <schema_path>")
        print("  schema_path: Path to XSD file or directory")
        sys.exit(1)

    schema_path = Path(sys.argv[1])

    # Create analyzer
    analyzer = XSDSchemaAnalyzer()

    # Parse schemas
    print(f"Parsing schemas from: {schema_path}")
    analyzer.parse_schemas([schema_path])

    # Build relationships
    analyzer.build_relationships()

    # Example queries
    print("\n" + "="*80)
    print("EXAMPLE QUERIES")
    print("="*80)

    # Find some abstract elements
    abstract = list(analyzer.get_abstract_elements())[:3]
    print(f"\nFound {len(analyzer.get_abstract_elements())} abstract elements")

    if abstract:
        for elem_qname in abstract:
            print(f"\nAbstract element: {elem_qname[0]}:{elem_qname[1]}")
            impls = analyzer.get_implementations(elem_qname)
            print(f"  Implementations ({len(impls)}): {[f'{q[0]}:{q[1]}' for q in sorted(impls)][:5]}...")

    # Example: combined attributes for a type (replace with a real type present in your analysis)
    # sample_type = ('netex', 'VersionOfObjectRefStructure')
    # print("\nCombined attributes for", sample_type)
    # print(analyzer.get_combined_attributes(sample_type))

    # Export to JSON
    output_path = Path("xsd_analysis_complete.json")
    analyzer.export_to_json(output_path)


if __name__ == "__main__":
    main()

