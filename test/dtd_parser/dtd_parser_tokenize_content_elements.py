import unittest
from src.dtd_parser.dtd_parser import DTDParser
from src.project_path.project_path import ProjectPath


class TestDTDParserTokenizeContent(unittest.TestCase):
    def setUp(self) -> None:
        self.dataPath = ProjectPath.get_project_data_dtd_path()

    def test_0(self):
        parser = DTDParser()
        parser.load(self.dataPath / '1element.dtd')
        self.assertEqual(len(parser._tokens), 1)

    def test_1(self):
        parser = DTDParser()
        parser.load(self.dataPath / '2nested_elements.dtd')
        self.assertEqual(len(parser._tokens), 2)

    def test_2(self):
        parser = DTDParser()
        parser.load(self.dataPath / '5nested_elements.dtd')
        self.assertEqual(len(parser._tokens), 5)
