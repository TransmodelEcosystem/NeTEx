"""
XSD Schema Dependency Analyzer
Builds an inverted dependency graph showing which elements depend on a given element
through type hierarchy (extension/restriction relationships).
"""

import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, Set, List
from collections import defaultdict
import json


class XSDDependencyAnalyzer:
    """Analyzes XSD schemas to build inverted dependency graphs based on type hierarchies."""

    XSD_NS = "http://www.w3.org/2001/XMLSchema"

    def __init__(self):
        # Element name -> its type name (or inline type identifier)
        self.element_to_type = {}

        # Type name -> its base type name (for extensions/restrictions)
        self.type_hierarchy = {}

        # Element name -> set of elements that depend on it (through type hierarchy)
        self.element_dependencies = defaultdict(set)

        # For debugging: store type derivation info
        self.type_info = {}
        
        # Abstract Elements
        self.abstract_elements = set([])
        self.substitutionGroups: dict[str, set[str]] = {}

    def parse_schemas(self, schema_paths: List[Path]) -> None:
        """Parse all XSD schemas from the given paths."""
        for path in schema_paths:
            if path.is_file():
                self._parse_schema_file(path)
            elif path.is_dir():
                for xsd_file in path.rglob("*.xsd"):
                    if 'xsd/netex' in str(xsd_file):
                        self._parse_schema_file(xsd_file)

    def _parse_schema_file(self, filepath: Path) -> None:
        """Parse a single XSD schema file."""
        try:
            tree = ET.parse(filepath)
            root = tree.getroot()

            # First pass: collect all type definitions
            self._extract_types(root)

            # Second pass: collect elements and their types
            self._extract_elements(root)

        except Exception as e:
            print(f"Error parsing {filepath}: {e}")

    def _extract_types(self, root: ET.Element) -> None:
        """Extract all type definitions and their base types."""
        # Complex types
        for ctype in root.findall(f".//{{{self.XSD_NS}}}complexType"):
            name = ctype.get('name')
            if not name:
                continue

            base_type = None
            derivation = None

            # Check for extension
            extension = ctype.find(f".//{{{self.XSD_NS}}}extension")
            if extension is not None:
                base_type = self._strip_ns(extension.get('base', ''))
                derivation = 'extension'

            # Check for restriction
            restriction = ctype.find(f".//{{{self.XSD_NS}}}restriction")
            if restriction is not None:
                base_type = self._strip_ns(restriction.get('base', ''))
                derivation = 'restriction'

            if base_type:
                self.type_hierarchy[name] = base_type
                self.type_info[name] = {'base': base_type, 'derivation': derivation}

        # Simple types
        for stype in root.findall(f".//{{{self.XSD_NS}}}simpleType"):
            name = stype.get('name')
            if not name:
                continue

            restriction = stype.find(f"{{{self.XSD_NS}}}restriction")
            if restriction is not None:
                base_type = self._strip_ns(restriction.get('base', ''))
                self.type_hierarchy[name] = base_type
                self.type_info[name] = {'base': base_type, 'derivation': 'restriction'}

    def _extract_elements(self, root: ET.Element) -> None:
        """Extract all element definitions and map them to their types."""
        for elem in root.findall(f".//{{{self.XSD_NS}}}element"):
            name = elem.get('name')
            if not name:
                continue
            
            substitutionGroup = elem.get('substitutionGroup', False)
            type_ref = elem.get('type', False)
            complex_type = elem.find(f"{{{self.XSD_NS}}}complexType")
            if not type_ref and not substitutionGroup and complex_type is None:
                continue

            abstract = elem.get('abstract', False)
            if abstract:
                self.abstract_elements.add(name)

            substitutionGroup = elem.get('substitutionGroup', False)
            if substitutionGroup:
                l = self.substitutionGroups.get(name, set([]))
                l.add(substitutionGroup)
                self.substitutionGroups[name] = l

            # Check for direct type reference
            type_ref = elem.get('type')
            if type_ref:
                self.element_to_type[name] = self._strip_ns(type_ref)
                continue

            # Check for inline complex type
            complex_type = elem.find(f"{{{self.XSD_NS}}}complexType")
            if complex_type is not None:
                # Look for restriction or extension in inline type
                restriction = complex_type.find(f".//{{{self.XSD_NS}}}restriction")
                extension = complex_type.find(f".//{{{self.XSD_NS}}}extension")

                if restriction is not None:
                    base_type = self._strip_ns(restriction.get('base', ''))
                    if base_type:
                        # Create a synthetic type name for the inline type
                        inline_type_name = f"{name}_InlineType"
                        self.element_to_type[name] = inline_type_name
                        self.type_hierarchy[inline_type_name] = base_type
                        self.type_info[inline_type_name] = {'base': base_type, 'derivation': 'restriction'}

                elif extension is not None:
                    base_type = self._strip_ns(extension.get('base', ''))
                    if base_type:
                        inline_type_name = f"{name}_InlineType"
                        self.element_to_type[name] = inline_type_name
                        self.type_hierarchy[inline_type_name] = base_type
                        self.type_info[inline_type_name] = {'base': base_type, 'derivation': 'extension'}

    def _strip_ns(self, qname: str) -> str:
        """Strip namespace prefix from a qualified name."""
        if ':' in qname:
            return qname.split(':', 1)[1]
        return qname

    def build_dependency_graph(self) -> None:
        """Build the inverted dependency graph with transitive relationships through element-specific types."""
        # First, build direct dependencies between element-specific types
        direct_deps = defaultdict(set)

        for elem_name in self.element_to_type.keys():
            elem_specific_types = self._get_element_specific_types(elem_name)
            if not elem_specific_types:
                continue

            for other_elem_name in self.element_to_type.keys():
                if other_elem_name == elem_name:
                    continue

                other_specific_types = self._get_element_specific_types(other_elem_name)

                # Check if any of the other element's specific types extend this element's specific types
                for other_spec_type in other_specific_types:
                    base = self.type_hierarchy.get(other_spec_type)
                    if base and base in elem_specific_types:
                        direct_deps[elem_name].add(other_elem_name)
                        break

        # Now compute transitive closure: if B depends on A, and C depends on B, then C depends on A
        self.element_dependencies = self._compute_transitive_closure(direct_deps)

    def _compute_transitive_closure(self, direct_deps: Dict[str, Set[str]]) -> Dict[str, Set[str]]:
        """Compute transitive closure of dependencies."""
        result = defaultdict(set)

        # Start with direct dependencies
        for elem, deps in direct_deps.items():
            result[elem] = set(deps)

        # Add transitive dependencies
        changed = True
        while changed:
            changed = False
            for elem in list(result.keys()):
                current_deps = set(result[elem])
                for dep in current_deps:
                    # If dep has its own dependencies, add them to elem's dependencies
                    if dep in result:
                        for transitive_dep in result[dep]:
                            if transitive_dep not in result[elem]:
                                result[elem].add(transitive_dep)
                                changed = True

        return result

    def _get_element_specific_types(self, elem_name: str) -> Set[str]:
        """Get types that are specific to this element (contain the element name in the type name)."""
        specific_types = set()

        elem_type = self.element_to_type.get(elem_name)
        if not elem_type:
            return specific_types

        # Start with the element's direct type
        current_type = elem_type

        # Walk up the type hierarchy and collect types that contain the element name
        while current_type:
            # Check if this type name contains the element name
            # For example: "ScheduledStopPoint_VersionStructure" contains "ScheduledStopPoint"
            if elem_name in current_type:
                specific_types.add(current_type)
            else:
                # Stop when we hit a generic type that doesn't contain the element name
                break

            current_type = self.type_hierarchy.get(current_type)

        return specific_types

    def _get_type_chain(self, elem_name: str) -> List[str]:
        """Get the complete type hierarchy chain for an element (most specific to most general)."""
        chain = []

        current_type = self.element_to_type.get(elem_name)
        if not current_type:
            return chain

        # Follow the type hierarchy up
        while current_type:
            chain.append(current_type)
            current_type = self.type_hierarchy.get(current_type)

        return chain

    def _depends_on(self, derived_chain: List[str], base_chain: List[str]) -> bool:
        """Check if derived_chain extends base_chain through shared type hierarchy."""
        if not base_chain or not derived_chain:
            return False

        # Check if any type from base_chain appears in derived_chain
        # If it does, and there are types before it in derived_chain,
        # then derived depends on base
        for base_type in base_chain:
            if base_type in derived_chain:
                derived_idx = derived_chain.index(base_type)
                # If the shared type appears later in derived chain (index > 0),
                # it means derived extends/restricts through this shared type
                if derived_idx > 0:
                    return True

        return False

    def get_dependents(self, element_name: str) -> Set[str]:
        """Get all elements that depend on the given element."""
        return self.element_dependencies.get(element_name, set())

    def get_dependency_path(self, base_elem: str, derived_elem: str) -> str:
        """Get the type hierarchy path showing the dependency (direct or transitive)."""
        base_specific_types = self._get_element_specific_types(base_elem)
        derived_specific_types = self._get_element_specific_types(derived_elem)

        if not base_specific_types or not derived_specific_types:
            return "No element-specific type information"

        # Check for direct connection
        for derived_type in derived_specific_types:
            base_of_derived = self.type_hierarchy.get(derived_type)
            if base_of_derived and base_of_derived in base_specific_types:
                derivation = self.type_info.get(derived_type, {}).get('derivation', 'unknown')
                return f"{derived_type} --[{derivation}]--> {base_of_derived} (direct)"

        # Check for transitive connection through intermediate elements
        # Find elements that derived depends on and that depend on base
        for intermediate in self.element_to_type.keys():
            if intermediate == base_elem or intermediate == derived_elem:
                continue

            intermediate_specific = self._get_element_specific_types(intermediate)

            # Check if derived extends intermediate
            derived_extends_intermediate = False
            for derived_type in derived_specific_types:
                base_of_derived = self.type_hierarchy.get(derived_type)
                if base_of_derived and base_of_derived in intermediate_specific:
                    derived_extends_intermediate = True
                    break

            # Check if intermediate extends base
            intermediate_extends_base = False
            for inter_type in intermediate_specific:
                base_of_inter = self.type_hierarchy.get(inter_type)
                if base_of_inter and base_of_inter in base_specific_types:
                    intermediate_extends_base = True
                    break

            if derived_extends_intermediate and intermediate_extends_base:
                return f"via {intermediate} (transitive)"

        return "No connection found"

    def print_all_dependencies(self) -> None:
        """Print dependency information for all elements."""
        print("\n" + "="*80)
        print("INVERTED DEPENDENCY GRAPH")
        print("="*80)

        for elem_name in sorted(self.element_to_type.keys()):
            dependents = self.get_dependents(elem_name)
            if dependents:
                print(f"\n{elem_name}:")
                print(f"  Type chain: {' → '.join(self._get_type_chain(elem_name))}")
                print(f"  Depended on by:")
                for dep in sorted(dependents):
                    path = self.get_dependency_path(elem_name, dep)
                    print(f"    - {dep}")
                    print(f"      via: {path}")

    def print_dependencies(self, element_name: str) -> None:
        """Print dependency information for a specific element."""
        if element_name not in self.element_to_type:
            print(f"Element '{element_name}' not found in schemas.")
            return

        print(f"\n{'='*80}")
        print(f"Dependencies for: {element_name}")
        print(f"{'='*80}")

        type_chain = self._get_type_chain(element_name)
        print(f"\nType chain: {' → '.join(type_chain)}")

        # Show which types are considered "specific" to this element
        specific_types = self._get_element_specific_types(element_name)
        if specific_types:
            print(f"\nElement-specific types: {', '.join(sorted(specific_types))}")

        dependents = self.get_dependents(element_name)
        if dependents:
            print(f"\nElements that depend on '{element_name}':")
            for dep in sorted(dependents):
                path = self.get_dependency_path(element_name, dep)
                print(f"  - {dep}")
                print(f"    via: {path}")
        else:
            print(f"\nNo elements depend on '{element_name}'")
            print("(Only showing dependencies on element-specific types, not shared ancestor types)")

    def export_to_json(self, output_path: Path) -> None:
        """Export the dependency graph to JSON."""
        result = {}

        for elem_name in sorted(self.element_to_type.keys()):
            dependents = self.get_dependents(elem_name)
            if dependents or elem_name:  # Include all elements
                result[elem_name] = {
                    'type_chain': self._get_type_chain(elem_name),
                    'depended_on_by': [
                        {
                            'element': dep,
                            'via_type_chain': self.get_dependency_path(elem_name, dep)
                        }
                        for dep in sorted(dependents)
                    ]
                }

        with open(output_path, 'w') as f:
            json.dump(result, f, indent=2)

        print(f"\n{'='*80}")
        print(f"Exported dependency graph to: {output_path}")
        print(f"{'='*80}")

    def get_simple_graph(self, root_type: str = None) -> Dict[str, List[str]]:
        """
        Get a simple dictionary mapping element names to lists of dependent elements.

        Args:
            root_type: If specified, only include elements whose type chain ends with this type.
                      For example, 'EntityStructure' to filter entities.

        Returns:
            Dict mapping element_name -> [list of dependent element names]
        """
        result = {}

        for elem_name in sorted(self.element_to_type.keys()):
            # Filter by root type if specified
            if root_type:
                type_chain = self._get_type_chain(elem_name)
                if not type_chain or type_chain[-1] != root_type:
                    continue

            dependents = self.get_dependents(elem_name)
            result[elem_name] = sorted(dependents)

        return result

    def export_simple_graph(self, output_path: Path, root_type: str = None) -> None:
        """
        Export a simple dependency graph as a clean dictionary.

        Args:
            output_path: Path to save the JSON file
            root_type: If specified, only include elements whose type chain ends with this type
        """
        graph = self.get_simple_graph(root_type)

        with open(output_path, 'w') as f:
            json.dump({'graph': graph, 'abstract': list(self.abstract_elements)}, f, indent=2)

        filter_msg = f" (filtered to {root_type})" if root_type else ""
        print(f"\n{'='*80}")
        print(f"Exported simple dependency graph to: {output_path}{filter_msg}")
        print(f"Total elements: {len(graph)}")
        print(f"{'='*80}")


def main():
    """Example usage."""
    import sys

    if len(sys.argv) < 2:
        print("Usage: python xsd_analyzer.py <schema_path> [element_name]")
        print("  schema_path: Path to XSD file or directory")
        print("  element_name: (optional) Specific element to analyze")
        print("\nIf no element_name is provided, shows dependencies for ALL elements")
        sys.exit(1)

    schema_path = Path(sys.argv[1])
    element_name = sys.argv[2] if len(sys.argv) > 2 else None

    # Create analyzer
    analyzer = XSDDependencyAnalyzer()

    # Parse schemas
    print(f"Parsing schemas from: {schema_path}")
    if schema_path.is_file():
        analyzer.parse_schemas([schema_path])
    else:
        analyzer.parse_schemas([schema_path])

    print(f"Found {len(analyzer.element_to_type)} elements")
    print(f"Found {len(analyzer.type_hierarchy)} type relationships")

    # Build dependency graph
    print("Building dependency graph...")
    analyzer.build_dependency_graph()

    # Print results
    # if element_name:
    #    analyzer.print_dependencies(element_name)
    # else:
    #    analyzer.print_all_dependencies()
    
    # Export detailed JSON
    # output_path = Path("xsd_dependencies.json")
    # analyzer.export_to_json(output_path)

    # Export simple graph (all elements)
    simple_path = Path("xsd_simple_graph.json")
    analyzer.export_simple_graph(simple_path)

    # Export simple graph filtered to EntityStructure
    # entity_path = Path("xsd_entity_graph.json")
    # analyzer.export_simple_graph(entity_path, root_type="EntityStructure")

    # Show example of using the simple graph
    print("\nExample: Simple graph structure")
    print("="*80)
    graph = analyzer.get_simple_graph(root_type="EntityStructure")

    # Show a few examples
    shown = 0
    for elem, deps in list(graph.items())[:3]:
        if deps:  # Only show elements with dependencies
            print(f"graph['{elem}'] = {deps}")
            shown += 1
            if shown >= 3:
                break

    print(analyzer._get_type_chain('LinkRef'))

if __name__ == "__main__":
    main()
