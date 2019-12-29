import unittest
from src.dtd_parser.dtd_parser import DTDParser
from src.project_path.project_path import ProjectPath


class TestDTDParserReadFileContent(unittest.TestCase):
    def setUp(self) -> None:
        self.dataPath = ProjectPath.get_project_data_dtd_path()

    def test_file_not_found(self):
        self.assertRaises(FileNotFoundError, DTDParser, self.dataPath / '.file_does_not_exist_gibberish.dtd.')

    def test_0(self):
        parser = DTDParser(self.dataPath / '0.dtd')
        self.assertEqual(parser._content.strip(), "<!ELEMENT note (#PCDATA)>")

    def test_1(self):
        parser = DTDParser()
        parser.load(self.dataPath / '1.dtd')
        self.assertEqual(parser._content.strip(), "<!ELEMENT note (heading)>\n<!ELEMENT heading (#PCDATA)>")
