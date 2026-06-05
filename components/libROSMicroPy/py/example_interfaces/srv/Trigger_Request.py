from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Trigger_Request(Message):
    _TYPE_NAME = 'Trigger_Request'
    _TYPE_DEF = _TYPE_DEFS['Trigger_Request']
    _fields_and_field_types = {}

    def __init__(self):
        pass

dataMap = Trigger_Request.get_data_map()
