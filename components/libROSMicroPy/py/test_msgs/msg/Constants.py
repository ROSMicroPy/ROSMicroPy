from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Constants(Message):
    _TYPE_NAME = 'Constants'
    _TYPE_DEF = _TYPE_DEFS['Constants']
    _fields_and_field_types = {}
    BOOL_CONST = True
    BYTE_CONST = 50
    CHAR_CONST = 100
    FLOAT32_CONST = 1.125
    FLOAT64_CONST = 1.125
    INT8_CONST = -50
    UINT8_CONST = 200
    INT16_CONST = -1000
    UINT16_CONST = 2000
    INT32_CONST = -30000
    UINT32_CONST = 60000
    INT64_CONST = -40000000
    UINT64_CONST = 50000000

    def __init__(self):
        pass

dataMap = Constants.get_data_map()
