import unittest
from src.dtd_parser.dtd_parser import DTDParser
from src.project_path.project_path import ProjectPath


class TestDTDParserTokenizeContent(unittest.TestCase):
    def setUp(self) -> None:
        self.dataPath = ProjectPath.get_project_data_dtd_path()

    def test_empty_file(self):
        parser = DTDParser()
        self.assertRaises(ValueError, parser.load, self.dataPath / 'empty.dtd')
        self.assertEqual(len(parser._tokens), 0)
        self.assertEqual(parser._content, "")

    def test_not_dtd_file(self):
        parser = DTDParser()
        self.assertRaises(ValueError, parser.load, self.dataPath / 'not_dtd.txt')
        self.assertEqual(len(parser._tokens), 0)

    def test_invalid_tags(self):
        parser = DTDParser()
        self.assertRaises(ValueError, parser.load, self.dataPath / 'invalid_tags.dtd')
