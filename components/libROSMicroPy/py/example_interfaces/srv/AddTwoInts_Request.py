from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class AddTwoInts_Request(Message):
    _TYPE_NAME = 'AddTwoInts_Request'
    _TYPE_DEF = _TYPE_DEFS['AddTwoInts_Request']
    _fields_and_field_types = {'a': 'int64', 'b': 'int64'}

    def __init__(self, a=None, b=None):
        self['a'] = 0 if a is None else a
        self['b'] = 0 if b is None else b

dataMap = AddTwoInts_Request.get_data_map()
