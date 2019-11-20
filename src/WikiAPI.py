import requests
from src.XMLDocument import XMLDocument
import xml.etree.ElementTree as ET

class WikiAPI:
    def get_page_header_text(self, keyword: str) -> str:

        html_data = self.get_page_html(keyword)
        parser = XMLDocument()
        parser.open_from_string("<html>" + html_data + "</html>")

        content = parser.get_root()

        formated_text = []
        result: str = ""

        for el in content.iter():
            if el.tag == 'p':
                striped_text = [text.strip() for text in list(el.itertext())]
                formated_text = [item.replace('\n', '') for item in striped_text if item.startswith("[") is not True
                                 and item != '\n' and item != '']

                for el2 in formated_text:
                    result = result + " " + el2

            elif el.tag == 'h2':
                striped_text = [text.strip() for text in list(el.itertext())]
                formated_text = [item.replace('\n', '') for item in striped_text if item.startswith("[") is not True
                                 and item != '\n' and item != '' and item.startswith("edit") is not True
                                 and item.startswith("]") is not True]

                for el2 in formated_text:
                    result = result + " <h2>" + el2 + "</h2>"

        return result

    def get_page_header_text_image(self, keyword: str) -> str:

        html_data = self.get_page_html(keyword)
        parser = XMLDocument()
        parser.open_from_string("<html>" + html_data + "</html>")

        content = parser.get_root()

        formated_text = []
        result: str = ""

        for el in content.iter():
            if el.tag == 'p':
                striped_text = [text.strip() for text in list(el.itertext())]
                formated_text = [item.replace('\n', '') for item in striped_text if item.startswith("[") is not True
                                 and item != '\n' and item != '']

                for el2 in formated_text:
                    result = result + " " + el2

            elif el.tag == 'h2':
                striped_text = [text.strip() for text in list(el.itertext())]
                formated_text = [item.replace('\n', '') for item in striped_text if item.startswith("[") is not True
                                 and item != '\n' and item != '' and item.startswith("edit") is not True
                                 and item.startswith("]") is not True]

                for el2 in formated_text:
                    result = result + " <h2>" + el2 + "</h2>"
            elif el.tag == 'img':
                result = result + self.__get_img_attributes(el)

        return result

    def get_page_images(self, keyword: str) -> str:

        html_data = self.get_page_html(keyword)
        parser = XMLDocument()
        parser.open_from_string("<html>" + html_data + "</html>")

        content = parser.get_root()

        formated_text = []
        result: str = ""

        for el in content.iter():
            if el.tag == 'img':
                result = result + self.__get_img_attributes(el)
        return result

    def __get_img_attributes(self, element: ET.Element) -> str:

        src: str = element.attrib["src"]
        width: str = element.attrib["width"]
        height: str = element.attrib["height"]

        return '<img src="' + src + '" width="' + width + '" height="' + height + '"/>'

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
