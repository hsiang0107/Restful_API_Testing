import xml


class XMLParser:
    def __init__(self, xml_file_path):
        self.file_path = xml_file_path
        self.tree = xml.etree.ElementTree.parse(xml_file_path)
        self.root = self.tree.getroot()

    def find_element(self, element_path):
        return self.root.find(element_path)
    
    def set_attribute(self, element_path, name, value):
        element = self.find_element(element_path)
        element.set(name, value)
        print("Set '%s' = '%s' in %s under %s" % (name, value, element_path, self.file_path))
        
    def get_attribute_value(self, element_path, name):
        element = self.find_element(element_path)
        value = element.get(name)
        return value
        
    def get_text(self, element_path):
        element = self.find_element(element_path)
        value = element.text
        return value

    def set_text(self, element_path, text):
        element = self.find_element(element_path)
        element.text = text
        print("Set text = '%s' in %s under %s" % (text, element_path, self.file_path))
    
    def write(self):
        self.tree.write(self.file_path)


def get_text(xml_file_path, element_path):
    parser = XMLParser(xml_file_path)
    return parser.get_text(element_path)


def set_text(xml_file_path, element_path, text):
    parser = XMLParser(xml_file_path)
    parser.set_text(element_path, text)
    parser.write()


def get_attribute_value(xml_file_path, element_path, name):
    parser = XMLParser(xml_file_path)
    return parser.get_attribute_value(element_path, name)


def update_attribute(xml_file_path, element_path, name, value):
    parser = XMLParser(xml_file_path)
    parser.set_attribute(element_path, name, value)
    parser.write()


def add_attribute(xml_file_path, element_path, name, value, delimiter=','):
    parser = XMLParser(xml_file_path)
    current_value = parser.get_attribute_value(element_path, name)
    new_value = current_value + delimiter + value
    parser.set_attribute(element_path, name, new_value)
    parser.write()


def remove_attribute_value(xml_file_path, element_path, name, value, delimiter=','):
    parser = XMLParser(xml_file_path)
    values = parser.get_attribute_value(element_path, name)
    value_list = values.split(delimiter)
    if value in value_list:
        value_list.remove(value)
        new_value = delimiter.join(value_list)
        parser.set_attribute(element_path, name, new_value)
        parser.write()
