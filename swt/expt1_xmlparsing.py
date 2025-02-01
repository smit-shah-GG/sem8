import xml.etree.ElementTree as ET


# Example 1: Basic XML Parsing
def basic_parse(xml_file):
    try:
        # Parse the XML file
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Print basic information
        print(f"Root tag: {root.tag}")
        print(f"Root attributes: {root.attrib}")

        # Iterate through all elements
        for child in root:
            print(f"Child tag: {child.tag}, Attributes: {child.attrib}")

    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    except FileNotFoundError:
        print("XML file not found")


# Example 2: Finding Specific Elements
def find_elements(xml_file, tag_name):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Find all elements with specified tag
    elements = root.findall(f".//{tag_name}")

    for elem in elements:
        print(f"Found element: {elem.tag}")
        print(f"Text content: {elem.text}")
        print(f"Attributes: {elem.attrib}")


# Example 3: Modifying XML
def modify_xml(xml_file, output_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Add a new element
    new_element = ET.SubElement(root, "new_tag")
    new_element.text = "This is new content"
    new_element.set("attribute1", "value1")

    # Write modified XML to new file
    tree.write(output_file)


# Example 4: Creating XML from scratch
def create_xml():
    # Create root element
    root = ET.Element("root")

    # Create child element
    child = ET.SubElement(root, "child")
    child.text = "Child content"
    child.set("name", "child1")

    # Create another child
    child2 = ET.SubElement(root, "child")
    child2.text = "Another child"
    child2.set("name", "child2")

    # Create XML tree and write to file
    tree = ET.ElementTree(root)
    tree.write("new_xml.xml")


# Example 5: Parsing XML with namespaces
def parse_with_namespaces(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Get namespace map
    namespaces = dict([node for _, node in ET.iterparse(xml_file, events=["start-ns"])])

    # Use namespace in finding elements
    for elem in root.findall(".//{http://example.com/ns}tag", namespaces):
        print(f"Found element with namespace: {elem.tag}")


# Example usage with sample XML
if __name__ == "__main__":
    # Sample XML content for testing
    sample_xml = """<?xml version="1.0"?>
    <data>
        <person id="1">
            <name>John Doe</name>
            <age>30</age>
        </person>
        <person id="2">
            <name>Jane Smith</name>
            <age>25</age>
        </person>
    </data>
    """

    # Write sample XML to file
    with open("sample.xml", "w") as f:
        f.write(sample_xml)

    # Test the functions
    print("Basic parsing:")
    basic_parse("sample.xml")

    print("\nFinding elements:")
    find_elements("sample.xml", "name")

    print("\nModifying XML:")
    modify_xml("sample.xml", "modified.xml")

    print("\nCreating new XML:")
    create_xml()
