from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class UInt16(Message):
    _TYPE_NAME = 'UInt16'
    _TYPE_DEF = _TYPE_DEFS['UInt16']
    _fields_and_field_types = {'data': 'uint16'}

    def __init__(self, data=None):
        self['data'] = 0 if data is None else data

dataMap = UInt16.get_data_map()
