from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class MultiDOFJointTrajectoryPoint(Message):
    _TYPE_NAME = 'MultiDOFJointTrajectoryPoint'
    _TYPE_DEF = _TYPE_DEFS['MultiDOFJointTrajectoryPoint']
    _fields_and_field_types = {'transforms': 'Transform', 'velocities': 'Twist', 'accelerations': 'Twist', 'time_from_start': 'Duration'}

    def __init__(self, transforms=None, velocities=None, accelerations=None, time_from_start=None):
        self['transforms'] = [] if transforms is None else transforms
        self['velocities'] = [] if velocities is None else velocities
        self['accelerations'] = [] if accelerations is None else accelerations
        self['time_from_start'] = {} if time_from_start is None else time_from_start

dataMap = MultiDOFJointTrajectoryPoint.get_data_map()
