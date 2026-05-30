from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class JointTrajectoryPoint(Message):
    _TYPE_NAME = 'JointTrajectoryPoint'
    _TYPE_DEF = _TYPE_DEFS['JointTrajectoryPoint']
    _fields_and_field_types = {'positions': 'float64', 'velocities': 'float64', 'accelerations': 'float64', 'effort': 'float64', 'time_from_start': 'Duration'}

    def __init__(self, positions=None, velocities=None, accelerations=None, effort=None, time_from_start=None):
        self['positions'] = [] if positions is None else positions
        self['velocities'] = [] if velocities is None else velocities
        self['accelerations'] = [] if accelerations is None else accelerations
        self['effort'] = [] if effort is None else effort
        self['time_from_start'] = {} if time_from_start is None else time_from_start

dataMap = JointTrajectoryPoint.get_data_map()
