from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Int32(Message):
    _TYPE_NAME = 'Int32'
    _TYPE_DEF = _TYPE_DEFS['Int32']
    _fields_and_field_types = {'data': 'int32'}

    def __init__(self, data=None):
        self['data'] = 0 if data is None else data

dataMap = Int32.get_data_map()
