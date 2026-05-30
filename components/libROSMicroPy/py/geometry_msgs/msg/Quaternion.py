from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Quaternion(Message):
    _TYPE_NAME = 'Quaternion'
    _TYPE_DEF = _TYPE_DEFS['Quaternion']
    _fields_and_field_types = {'x': 'float64', 'y': 'float64', 'z': 'float64', 'w': 'float64'}

    def __init__(self, x=None, y=None, z=None, w=None):
        self['x'] = 0.0 if x is None else x
        self['y'] = 0.0 if y is None else y
        self['z'] = 0.0 if z is None else z
        self['w'] = 0.0 if w is None else w

dataMap = Quaternion.get_data_map()
