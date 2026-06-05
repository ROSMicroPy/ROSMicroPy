from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Strings(Message):
    _TYPE_NAME = 'Strings'
    _TYPE_DEF = _TYPE_DEFS['Strings']
    _fields_and_field_types = {'string_value': 'string', 'string_value_default1': 'string', 'string_value_default2': 'string', 'string_value_default3': 'string', 'string_value_default4': 'string', 'string_value_default5': 'string'}
    STRING_CONST = 'Hello world!'

    def __init__(self, string_value=None, string_value_default1=None, string_value_default2=None, string_value_default3=None, string_value_default4=None, string_value_default5=None):
        self['string_value'] = '' if string_value is None else string_value
        self['string_value_default1'] = '' if string_value_default1 is None else string_value_default1
        self['string_value_default2'] = '' if string_value_default2 is None else string_value_default2
        self['string_value_default3'] = '' if string_value_default3 is None else string_value_default3
        self['string_value_default4'] = '' if string_value_default4 is None else string_value_default4
        self['string_value_default5'] = '' if string_value_default5 is None else string_value_default5

dataMap = Strings.get_data_map()
