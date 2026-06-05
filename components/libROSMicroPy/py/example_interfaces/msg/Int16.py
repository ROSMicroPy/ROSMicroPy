from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Int16(Message):
    _TYPE_NAME = 'Int16'
    _TYPE_DEF = _TYPE_DEFS['Int16']
    _fields_and_field_types = {'data': 'int16'}

    def __init__(self, data=None):
        self['data'] = 0 if data is None else data

dataMap = Int16.get_data_map()
