from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class UInt8(Message):
    _TYPE_NAME = 'UInt8'
    _TYPE_DEF = _TYPE_DEFS['UInt8']
    _fields_and_field_types = {'data': 'uint8'}

    def __init__(self, data=None):
        self['data'] = 0 if data is None else data

dataMap = UInt8.get_data_map()
