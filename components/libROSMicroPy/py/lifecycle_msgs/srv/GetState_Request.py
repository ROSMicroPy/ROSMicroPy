from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GetState_Request(Message):
    _TYPE_NAME = 'GetState_Request'
    _TYPE_DEF = _TYPE_DEFS['GetState_Request']
    _fields_and_field_types = {}

    def __init__(self):
        pass

dataMap = GetState_Request.get_data_map()
