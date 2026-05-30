from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class UInt64(Message):
    _TYPE_NAME = 'UInt64'
    _TYPE_DEF = _TYPE_DEFS['UInt64']
    _fields_and_field_types = {'data': 'uint64'}

    def __init__(self, data=None):
        self['data'] = 0 if data is None else data

dataMap = UInt64.get_data_map()
