from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class ParameterValue(Message):
    _TYPE_NAME = 'ParameterValue'
    _TYPE_DEF = _TYPE_DEFS['ParameterValue']
    _fields_and_field_types = {'type': 'uint8', 'bool_value': 'bool', 'integer_value': 'int64', 'double_value': 'float64', 'string_value': 'string', 'byte_array_value': 'byte', 'bool_array_value': 'bool', 'integer_array_value': 'int64', 'double_array_value': 'float64', 'string_array_value': 'string'}

    def __init__(self, type=None, bool_value=None, integer_value=None, double_value=None, string_value=None, byte_array_value=None, bool_array_value=None, integer_array_value=None, double_array_value=None, string_array_value=None):
        self['type'] = 0 if type is None else type
        self['bool_value'] = False if bool_value is None else bool_value
        self['integer_value'] = 0 if integer_value is None else integer_value
        self['double_value'] = 0.0 if double_value is None else double_value
        self['string_value'] = '' if string_value is None else string_value
        self['byte_array_value'] = [] if byte_array_value is None else byte_array_value
        self['bool_array_value'] = [] if bool_array_value is None else bool_array_value
        self['integer_array_value'] = [] if integer_array_value is None else integer_array_value
        self['double_array_value'] = [] if double_array_value is None else double_array_value
        self['string_array_value'] = [] if string_array_value is None else string_array_value

dataMap = ParameterValue.get_data_map()
