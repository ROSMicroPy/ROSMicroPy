from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GetMap_Request(Message):
    _TYPE_NAME = 'GetMap_Request'
    _TYPE_DEF = _TYPE_DEFS['GetMap_Request']
    _fields_and_field_types = {}

    def __init__(self):
        pass

dataMap = GetMap_Request.get_data_map()
