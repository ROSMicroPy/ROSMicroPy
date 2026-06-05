from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GetAvailableTransitions_Request(Message):
    _TYPE_NAME = 'GetAvailableTransitions_Request'
    _TYPE_DEF = _TYPE_DEFS['GetAvailableTransitions_Request']
    _fields_and_field_types = {}

    def __init__(self):
        pass

dataMap = GetAvailableTransitions_Request.get_data_map()
