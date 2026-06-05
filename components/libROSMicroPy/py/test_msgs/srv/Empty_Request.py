from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Empty_Request(Message):
    _TYPE_NAME = 'Empty_Request'
    _TYPE_DEF = _TYPE_DEFS['Empty_Request']
    _fields_and_field_types = {}

    def __init__(self):
        pass

dataMap = Empty_Request.get_data_map()
