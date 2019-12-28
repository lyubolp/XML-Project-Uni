from enum import IntEnum


class DTDAttributeValueType(IntEnum):
    """
    Defines the attribute-value of a DTD Attribute
    """
    NONE = 0
    VALUE = 1
    REQUIRED = 2
    IMPLIED = 3
    FIXED = 4


class DTDAttributeType(IntEnum):
    """
    Defines the attribute-type of a DTD Attribute
    """
    NONE = 0
    CDATA = 1
    Enumerated = 2
    ID = 3
    IDREF = 4
    IDREFS = 5
    NMTOKEN = 6
    NMTOKENS = 7
    ENTITY = 8
    ENTITIES = 9
    NOTATION = 10
    xml = 11


def convert_dtd_attribute_typefrom_string(attribute_type: str) -> DTDAttributeType:
    return DTDAttributeType[attribute_type]


class DTDAttribute:
    def __init__(self, element_name: str = "", attribute_name: str = "",
                 attribute_type: DTDAttributeType = DTDAttributeType.NONE,
                 value_type: DTDAttributeValueType = DTDAttributeValueType.NONE, value: str = ""):
        self.element_name = element_name
        self.name = attribute_name
        self.attribute_type = attribute_type
        self.value_type = value_type
        self.value = value
        self.enumerated_values = []
        self.enumerated_default_value = ""

    def set_element_name(self, element_name: str):
        self.element_name = element_name

    def set_name(self, name: str):
        self.name = name

    def set_type(self, attribute_type):
        if isinstance(attribute_type, DTDAttributeType):
            self.attribute_type = attribute_type
        else:
            self.attribute_type = convert_dtd_attribute_typefrom_string(attribute_type)

    def set_value_type(self, value_type: DTDAttributeValueType):
        self.value_type = value_type

    def set_value(self, value: str):
        self.value = value

    def set_enumerated_values(self, enumerated_values: list):
        self.enumerated_values = enumerated_values

    def set_enumerated_default_value(self, enumerated_default_value: str):
        self.enumerated_default_value = enumerated_default_value

    def get_element_name(self):
        return self.element_name

    def get_name(self):
        return self.name

    def get_attribute_type(self):
        return self.attribute_type

    def get_value_type(self):
        return self.value_type

    def get_value(self):
        return self.value

    def get_enumerated_values(self):
        return self.enumerated_values

    def get_enumerated_default_value(self):
        return self.enumerated_default_value

    def print(self):
        print("Element: " + self.element_name)
        print("Attribute: " + self.name)
        print("Attribute Type: " + self.attribute_type.name)
        print("Value Type: " + self.value_type.name)
        print("Value: " + self.value)
        if self.attribute_type == DTDAttributeType.Enumerated:
            print("Enumerated values: ", end='')
            print(self.enumerated_values)
            print("Default value: " + self.enumerated_default_value)
        print()
