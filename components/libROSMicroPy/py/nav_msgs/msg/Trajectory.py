from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Trajectory(Message):
    _TYPE_NAME = 'Trajectory'
    _TYPE_DEF = _TYPE_DEFS['Trajectory']
    _fields_and_field_types = {'header': 'Header', 'points': 'TrajectoryPoint'}

    def __init__(self, header=None, points=None):
        self['header'] = {} if header is None else header
        self['points'] = [] if points is None else points

dataMap = Trajectory.get_data_map()
