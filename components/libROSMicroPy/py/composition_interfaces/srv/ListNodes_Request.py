from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class ListNodes_Request(Message):
    _TYPE_NAME = 'ListNodes_Request'
    _TYPE_DEF = _TYPE_DEFS['ListNodes_Request']
    _fields_and_field_types = {}

    def __init__(self):
        pass

dataMap = ListNodes_Request.get_data_map()
