import re
from src.dtd_attribute.dtd_attribute import *


def get_token_children(token: str):
    splitter = r'[\s,)(]'
    return list(filter(None, re.split(splitter, token)[2:-1]))


def get_token_name(token: str) -> str:
    splitter = r'\s+'
    return list(filter(None, re.split(splitter, token, 2)[1:-1]))[0]


def split_on_whitespace(token: str, splits: int) -> list:
    splitter = r'\s+'
    return list(re.split(splitter, token, splits))


class DTDParser:
    def __init__(self, path=None):
        self.path = path
        self.content = ""
        self.attributes = dict()
        self.elements = dict()
        self.tokens = dict()

        if self.path is not None:
            self.load(path)

    def reset_state(self):
        self.path = None
        self.content = ""
        self.elements = dict()
        self.attributes = dict()

    def set_path(self, path):
        self.path = path

    def load(self, path):
        self.reset_state()
        self.set_path(path)

        self.read_file_content()
        self.tokenize_content()
        self.parse_tokens()

        # self.debug_print_attributes()
        # self.debug_print_elements()

    def debug_print_attributes(self):
        for i in self.attributes.keys():
            for k in self.attributes[i]:
                k.print()

    def debug_print_elements(self):
        for i in self.elements.keys():
            print("Element: " + i + ", Children: ", end="")
            print(self.elements[i])

    def read_file_content(self):
        with open(self.path, "r") as file:
            self.content = file.read()

    def validate_content(self):
        if self.content == "":
            raise ValueError("There is no content to parse from file {}".format(self.path))

        xml_file_regex = r'^\s*<(.*?>\s*<)*.*?>\s*$'
        if not re.match(xml_file_regex, self.content):
            raise ValueError("The content of file {} is invalid DTD".format(self.path))

    def tokenize_content(self):
        self.validate_content()

        xml_tags_regex = r'<.*?>'
        self.tokens = re.findall(xml_tags_regex, self.content)

    def parse_tokens(self):
        for token in self.tokens:
            if token.startswith("<!ELEMENT"):
                self.add_element(token)
            elif token.startswith("<!ATTLIST"):
                self.add_attribute(token)

    def add_element(self, token):
        name = get_token_name(token)
        children = get_token_children(token)
        self.elements[name] = children

    def add_attribute(self, token):
        attribute = DTDAttribute()

        split_element_name = split_on_whitespace(token, 2)[1:]
        element_name = split_element_name[0]
        attribute.set_element_name(element_name)
        split_attribute_name = split_on_whitespace(split_element_name[1], 1)
        attribute.set_name(split_attribute_name[0])
        token_after_attribute_name = split_attribute_name[1]

        if token_after_attribute_name.startswith('('):
            # Enumerated attribute
            split_all = list(filter(None, re.split(r'[)(>|]+', token_after_attribute_name)))
            attribute.set_type(DTDAttributeType.Enumerated)
            attribute.set_value_type(DTDAttributeValueType.VALUE)
            attribute.set_enumerated_default_value(split_all[-1].strip('" '))
            attribute.set_enumerated_values([value.strip('" ') for value in split_all[:-1]])
        else:
            # Non-enumerated attribute
            split_type = split_on_whitespace(token_after_attribute_name, 1)
            attribute.set_type(split_type[0])
            token_after_type = split_type[1]
            if token_after_type.startswith('#FIXED'):
                # Fixed attribute
                attribute.set_value_type(DTDAttributeValueType.FIXED)
                attribute.set_value(list(filter(None, re.split(r'[\s>]+', token_after_type)))[1].strip('"'))
            else:
                if token_after_type.startswith("#REQUIRED"):
                    attribute.set_value_type(DTDAttributeValueType.REQUIRED)
                elif token_after_type.startswith("#IMPLIED"):
                    attribute.set_value_type(DTDAttributeValueType.IMPLIED)
                else:  # Default Value
                    attribute.set_value_type(DTDAttributeValueType.VALUE)
                    attribute.set_value(list(filter(None, re.split(r'[>]+', token_after_type)))[0].strip('"'))

        if element_name not in self.attributes.keys():
            self.attributes[element_name] = []
        self.attributes[element_name].append(attribute)
