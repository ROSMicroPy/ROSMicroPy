from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Empty_Response(Message):
    _TYPE_NAME = 'Empty_Response'
    _TYPE_DEF = _TYPE_DEFS['Empty_Response']
    _fields_and_field_types = {}

    def __init__(self):
        pass

dataMap = Empty_Response.get_data_map()
