from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class String(Message):
    _TYPE_NAME = 'String'
    _TYPE_DEF = _TYPE_DEFS['String']
    _fields_and_field_types = {'data': 'string'}

    def __init__(self, data=None):
        self['data'] = '' if data is None else data

dataMap = String.get_data_map()
