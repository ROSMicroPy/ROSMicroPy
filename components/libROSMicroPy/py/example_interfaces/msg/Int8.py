from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Int8(Message):
    _TYPE_NAME = 'Int8'
    _TYPE_DEF = _TYPE_DEFS['Int8']
    _fields_and_field_types = {'data': 'int8'}

    def __init__(self, data=None):
        self['data'] = 0 if data is None else data

dataMap = Int8.get_data_map()
