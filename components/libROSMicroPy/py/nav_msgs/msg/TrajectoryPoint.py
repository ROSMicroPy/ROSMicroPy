from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class TrajectoryPoint(Message):
    _TYPE_NAME = 'TrajectoryPoint'
    _TYPE_DEF = _TYPE_DEFS['TrajectoryPoint']
    _fields_and_field_types = {'header': 'Header', 'pose': 'Pose', 'velocity': 'Twist', 'acceleration': 'Accel', 'effort': 'Wrench'}

    def __init__(self, header=None, pose=None, velocity=None, acceleration=None, effort=None):
        self['header'] = {} if header is None else header
        self['pose'] = {} if pose is None else pose
        self['velocity'] = {} if velocity is None else velocity
        self['acceleration'] = {} if acceleration is None else acceleration
        self['effort'] = {} if effort is None else effort

dataMap = TrajectoryPoint.get_data_map()
