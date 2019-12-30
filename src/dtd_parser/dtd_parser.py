import re
from src.dtd_attribute.dtd_attribute import *
from src.dtd_element.dtd_element import *


DTD_ELEMENT_TAG_BEGINNING = "<!ELEMENT"
DTD_ATTRIBUTE_TAG_BEGINNING = "<!ATTLIST"


def _get_token_name(token: str) -> str:
    """
    Get the first element of a token separated by white space on both sides
    :param token: string representing DTD element or attribute, e.g. <!ELEMENT ...>
    :return: element-name split from a DTD token
    """
    splitter = r'\s+'
    return list(filter(None, re.split(splitter, token, 2)[1:-1]))[0]


def _split_on_whitespace(token: str, splits: int) -> list:
    """
    Split a token (string) on white space a number of times
    :param token: the string to split on whitespace
    :param splits: how many splits to do
    :return: list of split substrings from the token
    """
    splitter = r'\s+'
    return list(re.split(splitter, token, splits))


class DTDParser:
    def __init__(self, path=None):
        self._path = path
        self._content = ""
        self._tokens = dict()
        self.attributes = dict()
        self.elements = dict()

        if self._path is not None:
            self.load(path)

    def _reset_state(self) -> None:
        """
        CLear the object state in order to allow a
        new file to be loaded
        """
        self._path = None
        self._content = ""
        self._tokens = dict()
        self.elements = dict()
        self.attributes = dict()

    def load(self, path) -> None:
        """
        Load a file from a path and parse its content
        :param path: path to the file to load
        """
        self._reset_state()
        self._path = path

        self._read_file_content()
        self._tokenize_content()
        self._parse_tokens()

    def _read_file_content(self) -> None:
        """
        Read the content of the file pointed by _path as a string
        """
        with open(self._path, "r") as file:
            self._content = file.read()

    def _validate_content(self) -> None:
        """
        Validate the read content of a file to make sure it's
        valid DTD-looking file. A DTD-looking file is a file which consists
        of xml-tags, aka all the content is enclosed in < and >
        e.g <a><b></a>
        This does not check for closing tags or if the DTD tags are valid
        """
        if self._content == "":
            raise ValueError("There is no content to parse from file {}".format(self._path))

        "xml_file_regex matches a string consisting of xml tags"
        xml_file_regex = r'^\s*<(.*?>\s*<)*.*?>\s*$'
        if not re.match(xml_file_regex, self._content):
            raise ValueError("The content of file {} is invalid DTD".format(self._path))

    def _tokenize_content(self) -> None:
        """
        Convert the content of the file to tokens which can then be parsed as
        valid elements or attributes. A token is each string enclosed in
        < and >
        """
        self._validate_content()

        "xml_tags_regex matches every XML tag separately"
        xml_tags_regex = r'<.*?>'
        self._tokens = re.findall(xml_tags_regex, self._content)

    def _parse_tokens(self) -> None:
        """
        Convert tokens (strings) into objects
        DTD Elements are converted into a dictionary with
            key: element name
            value: list of names of child elements
        DTD attributes are stored in a dictionary with
            key: element name, which this attribute belongs to
            value: list of DTDAttribute objects representing the parsed attributes
        """
        for token in self._tokens:
            if token.startswith(DTD_ELEMENT_TAG_BEGINNING):
                self._add_element(token)
            elif token.startswith(DTD_ATTRIBUTE_TAG_BEGINNING):
                self._add_attribute(token)
            else:
                raise ValueError("The content of file {} is invalid. Invalid token found: {}".format(self._path, token))

    def _add_element(self, token: str) -> None:
        """
        Parse a string, which is a DTD element, into a key-value pair
            key: element name
            value: child elements of this element
        :param token: string representing DTD element, e.g. <!ELEMENT ...>
        """
        name = _get_token_name(token)
        children = self._get_token_children(token)
        self.elements[name] = children

    def _add_attribute(self, token: str) -> None:
        """
        Parse a string, which is a DTD attribute, into a key-value pair
            key: element name, which this attribute belongs to
            value: DTDAttribute object (the parsed attribute)
        :param token: string representing a DTD attribute, e.g. <!ATTLIST ...>
        """
        attribute = DTDAttribute()

        split_element_name = _split_on_whitespace(token, 2)[1:]
        element_name = split_element_name[0]
        attribute.element_name = element_name
        split_attribute_name = _split_on_whitespace(split_element_name[1], 1)
        attribute.attribute_name = split_attribute_name[0]
        token_after_attribute_name = split_attribute_name[1]

        if token_after_attribute_name.startswith('('):
            # Enumerated attribute
            split_all = list(filter(None, re.split(r'[)(>|]+', token_after_attribute_name)))
            attribute.attribute_type = DTDAttributeType.Enumerated
            attribute.value_type = DTDAttributeValueType.VALUE
            attribute.enumerated_default_value = split_all[-1].strip('" ')
            attribute.enumerated_values = [value.strip('" ') for value in split_all[:-1]]
        else:
            # Non-enumerated attribute
            split_type = _split_on_whitespace(token_after_attribute_name, 1)
            attribute.attribute_type = convert_dtd_attribute_type_from_string(split_type[0])
            token_after_type = split_type[1]
            if token_after_type.startswith('#FIXED'):
                # Fixed attribute
                attribute.value_type = DTDAttributeValueType.FIXED
                attribute.value = list(filter(None, re.split(r'[\s>]+', token_after_type)))[1].strip('"')
            else:
                if token_after_type.startswith("#REQUIRED"):
                    attribute.value_type = DTDAttributeValueType.REQUIRED
                elif token_after_type.startswith("#IMPLIED"):
                    attribute.value_type = DTDAttributeValueType.IMPLIED
                else:  # Default Value
                    attribute.value_type = DTDAttributeValueType.VALUE
                    attribute.value = list(filter(None, re.split(r'[>]+', token_after_type)))[0].strip('"')

        if element_name not in self.attributes.keys():
            self.attributes[element_name] = []
        self.attributes[element_name].append(attribute)

    def _get_token_children(self, token: str):
        """
        Parse the child elements of a DTD element.
        Child elements are after the second whitespace
        :param token: string representing DTD element, e.g. <!ELEMENT ...>
        :return: list of all children of a DTD element
        """
        splitter = r'[\s]'
        children_string = re.split(splitter, token, 2)
        children_string = list(filter(None, children_string))[2]
        children_string = children_string.strip(">")
        "child_token_splitter is a regex which splits the children string into tokens"
        "a token is either a DTD element name or one of the following symbols:"
        "* ? + ( ) ,"
        child_token_splitter = r'[\+)(\,\*\?]|[^\+)(\,\*\?]+'
        children_list = re.findall(child_token_splitter, children_string)
        children_list = [x.strip(" ") for x in children_list]
        children_list = list(filter(None, children_list))

        root = DTDElement()
        current_element = root
        parents = []

        if children_list[0] == "EMPTY":
            root.element_name = "EMPTY"
            return root

        if children_list[-1] == "+":
            root.occurrences = DTDElementCount.OneOrMore
            children_list.pop(-1)
        if children_list[-1] == "*":
            root.occurrences = DTDElementCount.ZeroOrMore
            children_list.pop(-1)
        if children_list[-1] == "?":
            root.occurrences = DTDElementCount.ZeroOrOne
            children_list.pop(-1)

        if children_list[0] != "(" or children_list[-1] != ")":
            raise ValueError("Invalid DTD element {} in file {}".format(token, self._path))

        # Remove starting and ending parentheses, because the root is created manually
        children_list.pop(0)
        children_list.pop(-1)

        for child_token in children_list:
            if child_token == ",":
                pass
            elif child_token == "*":
                current_element.sub_elements[-1].occurrences = DTDElementCount.ZeroOrMore
            elif child_token == "+":
                current_element.sub_elements[-1].occurrences = DTDElementCount.OneOrMore
            elif child_token == "?":
                current_element.sub_elements[-1].occurrences = DTDElementCount.ZeroOrOne
            elif child_token == "(":
                new_child = DTDElement()
                current_element.sub_elements.append(new_child)
                parents.append(current_element)
                current_element = current_element.sub_elements[-1]
            elif child_token == ")":
                current_element = parents[-1]
                parents.pop(-1)
            else:
                new_child = DTDElement(child_token)
                current_element.sub_elements.append(new_child)

        return root

        # def _debug_print_attributes(self) -> None:
        #     """
        #     Print debug information about the attributes parsed on stdout
        #     """
        #     for i in self.attributes.keys():
        #         for k in self.attributes[i]:
        #             k._debug_print()
        #
        # def _debug_print_elements(self) -> None:
        #     """
        #     Print debug information about the elements parsed on stdout
        #     """
        #     for i in self.elements.keys():
        #         print("Element: " + i + ", Children: ", end="")
        #         print(self.elements[i])
