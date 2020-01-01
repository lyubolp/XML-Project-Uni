import unittest
from src.wiki_api.wiki_api import WikiAPI, Content, Image, XMLDocument


class TestWikiAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.instance = WikiAPI()
        self.article_name = 'Димитър Маджаров'

    def test_basic(self):
        self.assertEqual(2+3, 5)

    def test_get_text(self):
        self.assertEqual(self.instance.get_page_text(self.article_name).content[0][1],
                         'Димитър Петков Маджаров, наричан Маришки, '
                         'е български революционер и войвода на Вътрешната македоно-одринска революционна организация'
                         ' и на Вътрешната тракийска революционна организация. ')


