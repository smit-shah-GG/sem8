import xml.etree.ElementTree as ET
import time
import os
import gzip
import bz2
import json
from typing import Dict, Any


class XMLProcessor:
    def __init__(self, xml_file: str):
        self.xml_file = xml_file
        self.tree = None
        self.root = None
        self.load_xml()

    def load_xml(self):
        """Load XML file and get root element"""
        try:
            self.tree = ET.parse(self.xml_file)
            self.root = self.tree.getroot()
        except Exception as e:
            print(f"Error loading XML: {e}")

    def get_root(self):
        """1. Get the root element"""
        return self.root

    def get_first_child(self):
        """2. Get the first child of root element"""
        return list(self.root)[0] if len(list(self.root)) > 0 else None

    def get_child_attributes(self, child):
        """3. Get the attribute for the child of the root element"""
        return child.attrib if child is not None else {}

    def print_tags_and_attributes(self):
        """4. Print all tags and attributes within child tags"""
        for child in self.root:
            print(f"Tag: {child.tag}")
            print(f"Attributes: {child.attrib}")
            for subchild in child:
                print(f"  Subtag: {subchild.tag}")
                print(f"  Subattributes: {subchild.attrib}")

    def print_text_within_tags(self):
        """5. Print text present within tags"""
        for elem in self.root.iter():
            if elem.text and elem.text.strip():
                print(f"{elem.tag}: {elem.text.strip()}")

    def iterate_specific_tags(self, tag_name: str):
        """6. Iterate through tags with specific name"""
        return self.root.findall(f".//{tag_name}")

    def add_element(
        self,
        parent_tag: str,
        new_tag: str,
        attributes: Dict[str, Any] = None,
        text: str = None,
    ):
        """7. Add element to XML"""
        parent = self.root.find(f".//{parent_tag}")
        if parent is not None:
            new_element = ET.SubElement(parent, new_tag)
            if attributes:
                for key, value in attributes.items():
                    new_element.set(key, value)
            if text:
                new_element.text = text
            self.tree.write(self.xml_file)
            return True
        return False

    def remove_element(self, tag_name: str, attribute: Dict[str, str] = None):
        """7. Remove element from XML"""
        for elem in self.root.findall(f".//{tag_name}"):
            if attribute is None or all(elem.get(k) == v for k, v in attribute.items()):
                elem.getparent().remove(elem)
        self.tree.write(self.xml_file)


class XMLSerializationComparison:
    def __init__(self, sample_data: str):
        self.sample_data = sample_data
        self.results = {}

    def save_formats(self):
        """2. Store XML in different formats"""
        # Standard XML
        with open("standard.xml", "w") as f:
            f.write(self.sample_data)

        # Compressed XML (CXML)
        with gzip.open("compressed.xml.gz", "wt") as f:
            f.write(self.sample_data)

        # Binary XML (BXML) - using bz2 compression as an example
        with bz2.open("binary.xml.bz2", "wt") as f:
            f.write(self.sample_data)

    def measure_sizes(self):
        """3. Measure file sizes"""
        self.results["sizes"] = {
            "standard": os.path.getsize("standard.xml"),
            "compressed": os.path.getsize("compressed.xml.gz"),
            "binary": os.path.getsize("binary.xml.bz2"),
        }

    def measure_processing_time(self):
        """4. Measure processing time"""

        def parse_file(file_path):
            start_time = time.time()
            tree = ET.parse(file_path)
            root = tree.getroot()
            return time.time() - start_time

        self.results["processing_times"] = {
            "standard": parse_file("standard.xml"),
            "compressed": None,  # Need special handling for compressed files
            "binary": None,  # Need special handling for binary files
        }

    def analyze_results(self):
        """5. Compare and analyze results"""
        print("\nData Size Analysis:")
        for format_name, size in self.results["sizes"].items():
            print(f"{format_name}: {size/1024:.2f} KB")

        print("\nProcessing Time Analysis:")
        for format_name, proc_time in self.results["processing_times"].items():
            if proc_time is not None:
                print(f"{format_name}: {proc_time:.4f} seconds")

        print("\nAdvantages and Disadvantages:")
        print("Standard XML:")
        print("+ Human readable")
        print("+ No special processing needed")
        print("- Larger file size")

        print("\nCompressed XML (CXML):")
        print("+ Smaller file size")
        print("+ Good for storage and transmission")
        print("- Requires decompression before processing")

        print("\nBinary XML (BXML):")
        print("+ Smallest file size")
        print("+ Efficient for machine processing")
        print("- Not human readable")
        print("- Requires special processing")


def main():
    # Sample XML data
    sample_xml = """<?xml version="1.0"?>
    <root>
        <person id="1">
            <name>John Doe</name>
            <age>30</age>
            <city>New York</city>
        </person>
        <person id="2">
            <name>Jane Smith</name>
            <age>25</age>
            <city>Los Angeles</city>
        </person>
    </root>
    """

    # Test XML Processing
    with open("test.xml", "w") as f:
        f.write(sample_xml)

    processor = XMLProcessor("test.xml")

    print("Root element:", processor.get_root().tag)
    print("First child:", processor.get_first_child().tag)
    print(
        "Child attributes:", processor.get_child_attributes(processor.get_first_child())
    )

    print("\nTags and Attributes:")
    processor.print_tags_and_attributes()

    print("\nText within tags:")
    processor.print_text_within_tags()

    print("\nPersons:")
    for person in processor.iterate_specific_tags("person"):
        print(person.attrib)

    # Test XML Serialization Comparison
    comparison = XMLSerializationComparison(sample_xml)
    comparison.save_formats()
    comparison.measure_sizes()
    comparison.measure_processing_time()
    comparison.analyze_results()


if __name__ == "__main__":
    main()
