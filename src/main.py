from xml.dom import minidom, minicompat
import xml

class XMLDocument:
    def __init__(self):
        self._doc = None

    def read(self, file_path: str):
        self._doc = minidom.parse(file_path)

    def get_element_from_tag_name(self, tag_name: str) -> xml.dom.minicompat.NodeList:
        return self._doc.getELementsByTagName(tag_name)

    def get_attribute_from_tag_name(self, attribute_name: str, tag_name: str) -> str:
        return self.get_element_from_tag_name(tag_name)[attribute_name].value

    def get_nth_attribute_from_tag_name(self, n: int, tag_name: str) -> str:
        return self.get_element_from_tag_name(tag_name)[n].value

    def get_data_from_tag_name(self, tag_name: str) -> str:
        return self.get_element_from_tag_name(tag_name).childNodes[0].data



if __name__ == "__main__":

