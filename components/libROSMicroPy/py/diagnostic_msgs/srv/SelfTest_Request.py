from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class SelfTest_Request(Message):
    _TYPE_NAME = 'SelfTest_Request'
    _TYPE_DEF = _TYPE_DEFS['SelfTest_Request']
    _fields_and_field_types = {}

    def __init__(self):
        pass

dataMap = SelfTest_Request.get_data_map()
