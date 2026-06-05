from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Byte(Message):
    _TYPE_NAME = 'Byte'
    _TYPE_DEF = _TYPE_DEFS['Byte']
    _fields_and_field_types = {'data': 'byte'}

    def __init__(self, data=None):
        self['data'] = 0 if data is None else data

dataMap = Byte.get_data_map()
