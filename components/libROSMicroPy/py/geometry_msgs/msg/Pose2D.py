from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Pose2D(Message):
    _TYPE_NAME = 'Pose2D'
    _TYPE_DEF = _TYPE_DEFS['Pose2D']
    _fields_and_field_types = {'x': 'float64', 'y': 'float64', 'theta': 'float64'}

    def __init__(self, x=None, y=None, theta=None):
        self['x'] = 0.0 if x is None else x
        self['y'] = 0.0 if y is None else y
        self['theta'] = 0.0 if theta is None else theta

dataMap = Pose2D.get_data_map()
