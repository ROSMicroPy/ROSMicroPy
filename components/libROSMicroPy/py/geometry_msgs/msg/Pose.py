from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Pose(Message):
    _TYPE_NAME = 'Pose'
    _TYPE_DEF = _TYPE_DEFS['Pose']
    _fields_and_field_types = {'position': 'Point', 'orientation': 'Quaternion'}

    def __init__(self, position=None, orientation=None):
        self['position'] = {} if position is None else position
        self['orientation'] = {} if orientation is None else orientation

dataMap = Pose.get_data_map()
