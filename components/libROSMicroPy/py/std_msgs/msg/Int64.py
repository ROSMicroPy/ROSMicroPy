from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Int64(Message):
    _TYPE_NAME = 'Int64'
    _TYPE_DEF = _TYPE_DEFS['Int64']
    _fields_and_field_types = {'data': 'int64'}

    def __init__(self, data=None):
        self['data'] = 0 if data is None else data

dataMap = Int64.get_data_map()
