import os
from xml.etree import ElementTree


# Schema.xml  <->  Sqlalchemy
# 'seq_integer'  <->  INTEGER
# 'string'  <->  VARCHAR
# 'unique_identifier'  <->  UNIQUEIDENTIFIER
# 'unicode_string'  <->  NVARCHAR
# 'smallint'  <->  SMALLINT
# 'integer'  <->  INTEGER
# 'date_time'  <->  DATETIME
# 'guid'  <->  CHAR
# 'boolean'  <->  BIT
# 'blob'  <->  IMAGE
# 'bigint'  <->  BIGINT
# 'seq_biginteger'  <->  BIGINT
# 'char'  <->  CHAR
# 'binary'  <->  BINARY
# 'unsignedByte'  <->  TINYINT
# 'text'  <->  TEXT(2147483647)

g_column_mapping = {'blob': 'IMAGE', 'guid': 'CHAR', 'text': 'TEXT', 'char': 'CHAR',
                    'bigint': 'BIGINT', 'binary': 'BINARY', 'string': 'VARCHAR',
                    'integer': 'INTEGER', 'boolean': 'BIT', 'smallint': 'SMALLINT',
                    'date_time': 'DATETIME', 'seq_integer': 'INTEGER',
                    'unsignedByte': 'TINYINT', 'unicode_string': 'NVARCHAR',
                    'seq_biginteger': 'BIGINT', 'unique_identifier': 'UNIQUEIDENTIFIER'}

g_default_size = {'guid': '36', 'text': '2147483647', 'char': '20',
                  'binary': '256'}


def setup_column_size(type, size):
    has_setting = True
    global g_column_mapping
    if g_column_mapping[type] in ['INTEGER', 'BIT', 'BIGINT', 'DATETIME', 'UNIQUEIDENTIFIER']:
        has_setting = False

    global g_default_size

    if size.upper() in ['DEFAULT', 'MAX']:
        if type in g_default_size:
            size = g_default_size[type]
        else:
            has_setting = False

    return '(%s)' % size if has_setting else ''


def setup_primary_key(is_primary, has_pk):
    if is_primary.upper() == 'PRIMARY':
        has_pk[0] = True
        return "primary_key=True"
    else:
        return None


def setup_nullable(nullable):
    if nullable.upper() == 'FALSE':
        return 'nullable=False'
    else:
        return None


def get_column_setting(attrib, has_pk):
    global g_column_mapping
    sqlalchemy_type = g_column_mapping[attrib['DataType'].strip()]

    if attrib['Name'] == 'ID':
        attrib['Name'] = 'id'
    text = "    %s = Column(" % attrib['Name']
    column_arg = sqlalchemy_type
    column_arg += setup_column_size(attrib['DataType'].strip(), attrib['DataLength'])
    is_primary_key = setup_primary_key(attrib['KeyType'], has_pk)
    nullable = setup_nullable(attrib['Nullable'])
    information = [x for x in [column_arg, is_primary_key, nullable] if x is not None]
    text += '%s)\n' % ', '.join(information)
    return text


def get_class_name(name):
    name = ''.join(name.split('_'))
    if name[0].islower():
        temp = list(name)
        name = ''.join([temp[0].upper()] + temp[1:])
    return name


def get_default_class_string(table_name):
    text = "class %s(Base):\n" % get_class_name(table_name)
    text += "    __tablename__ = '%s'\n" % table_name
    return text


# generate one file(schema_build_<build no>.txt contain all the model definition
# then to use file checking software to compare the newly generated with the existing one
# in order to find out which models needs to be modified or created
# remember to change the build_no when trying to generate new models against newer version of schema.xml
xml_root = ElementTree.parse(r'C:\Users\tmcm\Desktop\Schema.xml').getroot()
model_path = os.path.dirname(os.path.realpath(__file__)) + '/models/'
build_no = '3100'
with open(model_path + 'schema_build_%s.txt' % build_no, 'w') as f:
    for table in xml_root.findall('.//Database/SchemaTable/SchemaGroup/Table'):
        has_primary_key = [False]
        content = get_default_class_string(table.get('Name'))
        for elem in table.getiterator():
            if elem.tag == 'Attribute':
                content += get_column_setting(elem.attrib, has_primary_key)
        if not has_primary_key[0]:
            print("%s has no primary key" % table.get('Name'))
        f.write(content)
        f.write('\n')


# generate from models.<filename> import <class> into __init__.py
# after "from db import *  python can identify model directly
with open(os.path.dirname(os.path.realpath(__file__)) + '/__init__.py', 'w') as f:
    loading_text = 'from db.models.%s import %s\n'
    for file in os.listdir(model_path):
        if file.endswith('.py') and file != '__init__.py':
            module_name = file.split('.')[0]
            class_name = get_class_name(module_name)
            f.write(loading_text % (module_name, class_name))
