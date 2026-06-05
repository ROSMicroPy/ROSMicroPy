from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class BasicTypes(Message):
    _TYPE_NAME = 'BasicTypes'
    _TYPE_DEF = _TYPE_DEFS['BasicTypes']
    _fields_and_field_types = {'bool_value': 'bool', 'byte_value': 'byte', 'char_value': 'char', 'float32_value': 'float32', 'float64_value': 'float64', 'int8_value': 'int8', 'uint8_value': 'uint8', 'int16_value': 'int16', 'uint16_value': 'uint16', 'int32_value': 'int32', 'uint32_value': 'uint32', 'int64_value': 'int64', 'uint64_value': 'uint64'}

    def __init__(self, bool_value=None, byte_value=None, char_value=None, float32_value=None, float64_value=None, int8_value=None, uint8_value=None, int16_value=None, uint16_value=None, int32_value=None, uint32_value=None, int64_value=None, uint64_value=None):
        self['bool_value'] = False if bool_value is None else bool_value
        self['byte_value'] = 0 if byte_value is None else byte_value
        self['char_value'] = 0 if char_value is None else char_value
        self['float32_value'] = 0.0 if float32_value is None else float32_value
        self['float64_value'] = 0.0 if float64_value is None else float64_value
        self['int8_value'] = 0 if int8_value is None else int8_value
        self['uint8_value'] = 0 if uint8_value is None else uint8_value
        self['int16_value'] = 0 if int16_value is None else int16_value
        self['uint16_value'] = 0 if uint16_value is None else uint16_value
        self['int32_value'] = 0 if int32_value is None else int32_value
        self['uint32_value'] = 0 if uint32_value is None else uint32_value
        self['int64_value'] = 0 if int64_value is None else int64_value
        self['uint64_value'] = 0 if uint64_value is None else uint64_value

dataMap = BasicTypes.get_data_map()
