from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GetAvailableStates_Request(Message):
    _TYPE_NAME = 'GetAvailableStates_Request'
    _TYPE_DEF = _TYPE_DEFS['GetAvailableStates_Request']
    _fields_and_field_types = {}

    def __init__(self):
        pass

dataMap = GetAvailableStates_Request.get_data_map()
