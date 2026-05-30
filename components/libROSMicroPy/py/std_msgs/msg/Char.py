from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Char(Message):
    _TYPE_NAME = 'Char'
    _TYPE_DEF = _TYPE_DEFS['Char']
    _fields_and_field_types = {'data': 'char'}

    def __init__(self, data=None):
        self['data'] = 0 if data is None else data

dataMap = Char.get_data_map()
