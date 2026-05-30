from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class JointTrajectory(Message):
    _TYPE_NAME = 'JointTrajectory'
    _TYPE_DEF = _TYPE_DEFS['JointTrajectory']
    _fields_and_field_types = {'header': 'Header', 'joint_names': 'string', 'points': 'JointTrajectoryPoint'}

    def __init__(self, header=None, joint_names=None, points=None):
        self['header'] = {} if header is None else header
        self['joint_names'] = [] if joint_names is None else joint_names
        self['points'] = [] if points is None else points

dataMap = JointTrajectory.get_data_map()
