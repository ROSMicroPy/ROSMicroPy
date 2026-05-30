from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Empty(Message):
    _TYPE_NAME = 'Empty'
    _TYPE_DEF = _TYPE_DEFS['Empty']
    _fields_and_field_types = {}

    def __init__(self):
        pass

dataMap = Empty.get_data_map()
