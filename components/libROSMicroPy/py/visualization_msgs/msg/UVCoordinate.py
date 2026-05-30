from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class UVCoordinate(Message):
    _TYPE_NAME = 'UVCoordinate'
    _TYPE_DEF = _TYPE_DEFS['UVCoordinate']
    _fields_and_field_types = {'u': 'float32', 'v': 'float32'}

    def __init__(self, u=None, v=None):
        self['u'] = 0.0 if u is None else u
        self['v'] = 0.0 if v is None else v

dataMap = UVCoordinate.get_data_map()
