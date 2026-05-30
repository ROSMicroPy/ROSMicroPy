from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class ColorRGBA(Message):
    _TYPE_NAME = 'ColorRGBA'
    _TYPE_DEF = _TYPE_DEFS['ColorRGBA']
    _fields_and_field_types = {'r': 'float32', 'g': 'float32', 'b': 'float32', 'a': 'float32'}

    def __init__(self, r=None, g=None, b=None, a=None):
        self['r'] = 0.0 if r is None else r
        self['g'] = 0.0 if g is None else g
        self['b'] = 0.0 if b is None else b
        self['a'] = 0.0 if a is None else a

dataMap = ColorRGBA.get_data_map()
