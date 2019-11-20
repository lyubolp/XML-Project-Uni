import requests
from src.XMLDocument import XMLDocument
from src.Content import Content, ContentType
from src.Image import Image
import xml.etree.ElementTree as ET


class WikiAPI:
    def get_page_header_text(self, keyword: str) -> Content:
        content = self.__get_root_from_html(self.get_page_html(keyword))
        result: Content = Content()

        for current_element in content.iter():
            if current_element.tag == 'p':
                result.add_text(self.__get_text_from_element(current_element))
            elif current_element.tag == 'h2':
                result.add_title(self.__get_title_from_element(current_element))

        return result

    def get_page_header_image(self, keyword: str) -> Content:
        content = self.__get_root_from_html(self.get_page_html(keyword))
        result: Content = Content()

        for current_element in content.iter():
            if current_element.tag == 'h2':
                result.add_title(self.__get_title_from_element(current_element))
            elif current_element.tag == 'img':
                result.add_image(self.__get_img_attributes(current_element))

        return result

    def get_page_header_text_image(self, keyword: str) -> Content:
        content = self.__get_root_from_html(self.get_page_html(keyword))
        result: Content = Content()

        for current_element in content.iter():
            if current_element.tag == 'p':
                result.add_text(self.__get_text_from_element(current_element))
            elif current_element.tag == 'h2':
                result.add_title(self.__get_title_from_element(current_element))
            elif current_element.tag == 'img':
                result.add_image(self.__get_img_attributes(current_element))

        return result

    def get_page_text(self, keyword: str) -> Content:
        content = self.__get_root_from_html(self.get_page_html(keyword))
        result: Content = Content()

        for el in content.iter():
            if el.tag == 'p':
                result.add_text(self.__get_text_from_element(el))

        return result

    def get_page_images(self, keyword: str) -> Content:
        content = self.__get_root_from_html(self.get_page_html(keyword))
        result: Content = Content()

        for el in content.iter():
            if el.tag == 'img':
                result.add_image(self.__get_img_attributes(el))
        return result

    @staticmethod
    def __get_text_from_element(element: ET.Element) -> str:
        result = ""
        striped_text = [text.strip() for text in list(element.itertext())]
        formated_text = [item.replace('\n', '') for item in striped_text if item.startswith("[") is not True
                         and item != '\n' and item != '']

        for el2 in formated_text:
            result = result + " " + el2
        return result

    @staticmethod
    def __get_title_from_element(element: ET.Element) -> str:
        result = ""
        striped_text = [text.strip() for text in list(element.itertext())]
        formated_text = [item.replace('\n', '') for item in striped_text if item.startswith("[") is not True
                         and item != '\n' and item != '' and item.startswith("edit") is not True
                         and item.startswith("]") is not True]

        for el2 in formated_text:
            result = result + " " + el2
        return result

    @staticmethod
    def __get_root_from_html(html_data: str) -> ET.Element:
        parser = XMLDocument()
        parser.open_from_string("<html>" + html_data + "</html>")

        return parser.get_root()

    @staticmethod
    def __get_img_attributes(element: ET.Element) -> Image:

        src: str = element.attrib["src"]
        width: str = element.attrib["width"]
        height: str = element.attrib["height"]

        return Image(src, width, height)

    def get_page_html(self, keyword: str) -> str:
        S = requests.Session()

        URL = "https://en.wikipedia.org/w/api.php"

        PARAMS = {
            "action": "parse",
            "page": keyword,
            "format": "json"
        }

        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()

        html_data = DATA["parse"]["text"]["*"]

        return html_data
