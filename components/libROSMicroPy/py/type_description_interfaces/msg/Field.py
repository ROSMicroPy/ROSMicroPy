from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Field(Message):
    _TYPE_NAME = 'Field'
    _TYPE_DEF = _TYPE_DEFS['Field']
    _fields_and_field_types = {'name': 'string', 'type': 'FieldType', 'default_value': 'string'}

    def __init__(self, name=None, type=None, default_value=None):
        self['name'] = '' if name is None else name
        self['type'] = {} if type is None else type
        self['default_value'] = '' if default_value is None else default_value

dataMap = Field.get_data_map()
