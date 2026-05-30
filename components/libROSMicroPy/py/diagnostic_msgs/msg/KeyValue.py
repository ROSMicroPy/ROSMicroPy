from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class KeyValue(Message):
    _TYPE_NAME = 'KeyValue'
    _TYPE_DEF = _TYPE_DEFS['KeyValue']
    _fields_and_field_types = {'key': 'string', 'value': 'string'}

    def __init__(self, key=None, value=None):
        self['key'] = '' if key is None else key
        self['value'] = '' if value is None else value

dataMap = KeyValue.get_data_map()
