from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class WString(Message):
    _TYPE_NAME = 'WString'
    _TYPE_DEF = _TYPE_DEFS['WString']
    _fields_and_field_types = {'data': 'string'}

    def __init__(self, data=None):
        self['data'] = '' if data is None else data

dataMap = WString.get_data_map()
