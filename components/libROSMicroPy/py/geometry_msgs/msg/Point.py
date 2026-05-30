from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Point(Message):
    _TYPE_NAME = 'Point'
    _TYPE_DEF = _TYPE_DEFS['Point']
    _fields_and_field_types = {'x': 'float64', 'y': 'float64', 'z': 'float64'}

    def __init__(self, x=None, y=None, z=None):
        self['x'] = 0.0 if x is None else x
        self['y'] = 0.0 if y is None else y
        self['z'] = 0.0 if z is None else z

dataMap = Point.get_data_map()
