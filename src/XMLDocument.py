import xml.etree.ElementTree as ET

class XMLDocument:
    def __init__(self):
        self._doc = None
        self._root = None

    def open(self, file_path: str):
        self._doc = ET.parse(file_path)
        self._root = self._doc.getroot()
        self._path = file_path

    def open_from_string(self, xml_string: str):
        self._doc = ET.fromstring(xml_string)
        self._root = ET.fromstring(xml_string)
        self._path = "temp.xml"

    def save(self):
        data = ET.tostring(self._root).decode("utf-8")
        file = open(self._path, "w")
        file.write(data)

    def add_element(self, root: str, tag: str, content: str, attributes: dict = None):
        added_item = ET.SubElement(self.get_first_element(root), tag, attributes)
        added_item.text = content

    def add_attribute(self, tag: str, key_value: (str, str)):
        self.get_first_element(tag).attrib[key_value[0]] = key_value[1]

    def add_content(self, tag: str, content: str):
        self.get_first_element(tag).text = content

    def edit_element(self, old_tag: str, new_tag: str):
        self.get_first_element(old_tag).tag = new_tag

    def edit_attribute(self, tag: str, key_value: (str, str)):
        self.get_first_element(tag).attrib[key_value[0]] = key_value[1]

    def edit_content(self, tag: str, content: str):
        self.get_first_element(tag).text = content

    def get_elements(self, name: str) -> list:
        return self._root.findall(".//" + name)

    def get_first_element(self, name: str) -> ET.Element:
        return self._root.find(".//" + name)

    def get_attributes(self, tag: str) -> dict:
        return self.get_first_element(tag).attrib

    def get_content(self, tag: str) -> str:
        return self.get_first_element(tag).text

    def remove_element(self, tag: str):
        parent_of_element = self._root.find(".//" + tag + "/..")
        parent_of_element.remove(self.get_first_element(tag))

    def remove_attribute(self, tag: str, attribute_name: str):
        del self.get_attributes(tag)[attribute_name]

    def remove_content(self, tag: str):
        self.get_first_element(tag).text = None

