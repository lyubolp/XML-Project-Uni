import unittest
from src.dtd_parser.dtd_parser import DTDParser
from src.project_path.project_path import ProjectPath


class TestDTDParserTokenizeContent(unittest.TestCase):
    def setUp(self) -> None:
        self.dataPath = ProjectPath.get_project_data_dtd_path()

    def test_3(self):
        parser = DTDParser()
        parser.load(self.dataPath / '1element_6attributes.dtd')
        self.assertEqual(len(parser._tokens), 7)