from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class UInt32(Message):
    _TYPE_NAME = 'UInt32'
    _TYPE_DEF = _TYPE_DEFS['UInt32']
    _fields_and_field_types = {'data': 'uint32'}

    def __init__(self, data=None):
        self['data'] = 0 if data is None else data

dataMap = UInt32.get_data_map()
