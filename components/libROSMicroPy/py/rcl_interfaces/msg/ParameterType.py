from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class ParameterType(Message):
    _TYPE_NAME = 'ParameterType'
    _TYPE_DEF = _TYPE_DEFS['ParameterType']
    _fields_and_field_types = {}
    PARAMETER_NOT_SET = 0
    PARAMETER_BOOL = 1
    PARAMETER_INTEGER = 2
    PARAMETER_DOUBLE = 3
    PARAMETER_STRING = 4
    PARAMETER_BYTE_ARRAY = 5
    PARAMETER_BOOL_ARRAY = 6
    PARAMETER_INTEGER_ARRAY = 7
    PARAMETER_DOUBLE_ARRAY = 8
    PARAMETER_STRING_ARRAY = 9

    def __init__(self):
        pass

dataMap = ParameterType.get_data_map()
