from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GetInteractiveMarkers_Request(Message):
    _TYPE_NAME = 'GetInteractiveMarkers_Request'
    _TYPE_DEF = _TYPE_DEFS['GetInteractiveMarkers_Request']
    _fields_and_field_types = {}

    def __init__(self):
        pass

dataMap = GetInteractiveMarkers_Request.get_data_map()
