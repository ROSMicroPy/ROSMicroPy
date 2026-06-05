from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Arrays_Response(Message):
    _TYPE_NAME = 'Arrays_Response'
    _TYPE_DEF = _TYPE_DEFS['Arrays_Response']
    _fields_and_field_types = {'bool_values': 'bool', 'byte_values': 'byte', 'char_values': 'char', 'float32_values': 'float32', 'float64_values': 'float64', 'int8_values': 'int8', 'uint8_values': 'uint8', 'int16_values': 'int16', 'uint16_values': 'uint16', 'int32_values': 'int32', 'uint32_values': 'uint32', 'int64_values': 'int64', 'uint64_values': 'uint64', 'string_values': 'string', 'basic_types_values': 'BasicTypes', 'constants_values': 'Constants', 'defaults_values': 'Defaults', 'bool_values_default': 'bool', 'byte_values_default': 'byte', 'char_values_default': 'char', 'float32_values_default': 'float32', 'float64_values_default': 'float64', 'int8_values_default': 'int8', 'uint8_values_default': 'uint8', 'int16_values_default': 'int16', 'uint16_values_default': 'uint16', 'int32_values_default': 'int32', 'uint32_values_default': 'uint32', 'int64_values_default': 'int64', 'uint64_values_default': 'uint64', 'string_values_default': 'string'}

    def __init__(self, bool_values=None, byte_values=None, char_values=None, float32_values=None, float64_values=None, int8_values=None, uint8_values=None, int16_values=None, uint16_values=None, int32_values=None, uint32_values=None, int64_values=None, uint64_values=None, string_values=None, basic_types_values=None, constants_values=None, defaults_values=None, bool_values_default=None, byte_values_default=None, char_values_default=None, float32_values_default=None, float64_values_default=None, int8_values_default=None, uint8_values_default=None, int16_values_default=None, uint16_values_default=None, int32_values_default=None, uint32_values_default=None, int64_values_default=None, uint64_values_default=None, string_values_default=None):
        self['bool_values'] = [] if bool_values is None else bool_values
        self['byte_values'] = [] if byte_values is None else byte_values
        self['char_values'] = [] if char_values is None else char_values
        self['float32_values'] = [] if float32_values is None else float32_values
        self['float64_values'] = [] if float64_values is None else float64_values
        self['int8_values'] = [] if int8_values is None else int8_values
        self['uint8_values'] = [] if uint8_values is None else uint8_values
        self['int16_values'] = [] if int16_values is None else int16_values
        self['uint16_values'] = [] if uint16_values is None else uint16_values
        self['int32_values'] = [] if int32_values is None else int32_values
        self['uint32_values'] = [] if uint32_values is None else uint32_values
        self['int64_values'] = [] if int64_values is None else int64_values
        self['uint64_values'] = [] if uint64_values is None else uint64_values
        self['string_values'] = [] if string_values is None else string_values
        self['basic_types_values'] = [] if basic_types_values is None else basic_types_values
        self['constants_values'] = [] if constants_values is None else constants_values
        self['defaults_values'] = [] if defaults_values is None else defaults_values
        self['bool_values_default'] = [] if bool_values_default is None else bool_values_default
        self['byte_values_default'] = [] if byte_values_default is None else byte_values_default
        self['char_values_default'] = [] if char_values_default is None else char_values_default
        self['float32_values_default'] = [] if float32_values_default is None else float32_values_default
        self['float64_values_default'] = [] if float64_values_default is None else float64_values_default
        self['int8_values_default'] = [] if int8_values_default is None else int8_values_default
        self['uint8_values_default'] = [] if uint8_values_default is None else uint8_values_default
        self['int16_values_default'] = [] if int16_values_default is None else int16_values_default
        self['uint16_values_default'] = [] if uint16_values_default is None else uint16_values_default
        self['int32_values_default'] = [] if int32_values_default is None else int32_values_default
        self['uint32_values_default'] = [] if uint32_values_default is None else uint32_values_default
        self['int64_values_default'] = [] if int64_values_default is None else int64_values_default
        self['uint64_values_default'] = [] if uint64_values_default is None else uint64_values_default
        self['string_values_default'] = [] if string_values_default is None else string_values_default

dataMap = Arrays_Response.get_data_map()
