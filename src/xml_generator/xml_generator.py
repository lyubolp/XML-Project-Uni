from src.dtd_element.dtd_element import DTDElement, DTDElementCount
from src.dtd_attribute.dtd_attribute import DTDAttributeValueType, DTDAttributeType
from src.dtd_parser.dtd_parser import DTDParser
from src.xml_document import XMLDocument
import xml.etree.ElementTree as ET


class XMLGenerator:
    """
    XMLGenerator uses parsed DTD elements and attributes
    from dtd_parser object and generates an XML document
    in the form of a XMLDocument object
    """
    def __init__(self, parser: DTDParser):
        self._parser = parser
        self._root_name = parser.get_root()
        self._xml = XMLDocument()

    def generate_xml(self):
        self._xml = XMLDocument()
        self._xml.init_with_root(self._root_name)

        if self._root_name in self._parser.attributes.keys():
            for attr in self._parser.attributes[self._root_name]:
                self._xml.add_attribute(self._root_name, (attr.attribute_name, attr.value))

        if self._root_name in self._parser.elements.keys():
            children = self._parser.elements[self._root_name]
            if children.element_name == "":
                for child in children.sub_elements:
                    self._recursive_add_children(self._root_name, child)

    def _recursive_add_children(self, parent: str, child: DTDElement):
        if child.element_name != "":
            if child.element_name == "#PCDATA":
                return
            self._xml.add_element(parent, child.element_name, "")

            if child.element_name in self._parser.attributes.keys():
                for attr in self._parser.attributes[child.element_name]:
                    self._xml.add_attribute(child.element_name, (attr.attribute_name, attr.value))

            if child.element_name in self._parser.elements.keys():
                grand_children = self._parser.elements[child.element_name]
                if grand_children.element_name == "":
                    for grand_child in grand_children.sub_elements:
                        self._recursive_add_children(child.element_name,grand_child)
        else:
            for sub_child in child.sub_elements:
                self._recursive_add_children(parent, sub_child)


    def to_string(self):
        return str(ET.tostring(self._xml.get_root(), encoding="unicode", method="xml"))
