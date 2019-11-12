import xml.etree.ElementTree as ET

'''
    @TODO - add methods that accept an ET.Element as an argument
'''

class XMLDocument:
    # https://stackabuse.com/reading-and-writing-xml-files-in-python/
    def __init__(self):
        self._doc = None
        self._root = None

    def create(self):
        pass

    def open(self, file_path: str):
        self._doc = ET.parse(file_path)
        self._root = self._doc.getroot()
        self._path = file_path

    def save(self):
        data = ET.tostring(self._root).decode("utf-8")
        file = open(self._path, "w")
        file.write(data)

        self.open(self._path)

    def add_element(self, root: str, tag: str, content: str, attributes: dict = None) -> ET.Element:

        added_item = ET.SubElement(self.get_first_element(root), tag, attributes)
        added_item.text = content
        return added_item

    def add_attribute(self, tag: str, key_value: (str, str)):
        self.get_first_element(tag)

    def add_content(self):
        pass

    def edit_element(self):
        pass

    def edit_attribute(self):
        pass

    def edit_content(self):
        pass

    def get_elements(self, name: str) -> list:
        return self._root.findall(".//" + name)

    def get_first_element(self, name: str) -> ET.Element:
        return self._root.find(".//" + name)

    def get_attributes(self, tag: str) -> dict:
        return self.get_first_element(tag).attrib

    def get_content(self, tag: str) -> str:
        return self.get_first_element(tag).text

    def remove_element(self):
        pass

    def remove_attribute(self):
        pass

    def remove_content(self):
        pass

