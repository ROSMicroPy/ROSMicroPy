from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Odometry(Message):
    _TYPE_NAME = 'Odometry'
    _TYPE_DEF = _TYPE_DEFS['Odometry']
    _fields_and_field_types = {'header': 'Header', 'child_frame_id': 'string', 'pose': 'PoseWithCovariance', 'twist': 'TwistWithCovariance'}

    def __init__(self, header=None, child_frame_id=None, pose=None, twist=None):
        self['header'] = {} if header is None else header
        self['child_frame_id'] = '' if child_frame_id is None else child_frame_id
        self['pose'] = {} if pose is None else pose
        self['twist'] = {} if twist is None else twist

dataMap = Odometry.get_data_map()
