from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Bool(Message):
    _TYPE_NAME = 'Bool'
    _TYPE_DEF = _TYPE_DEFS['Bool']
    _fields_and_field_types = {'data': 'bool'}

    def __init__(self, data=None):
        self['data'] = False if data is None else data

dataMap = Bool.get_data_map()
