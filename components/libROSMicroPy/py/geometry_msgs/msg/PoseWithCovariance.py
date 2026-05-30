from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class PoseWithCovariance(Message):
    _TYPE_NAME = 'PoseWithCovariance'
    _TYPE_DEF = _TYPE_DEFS['PoseWithCovariance']
    _fields_and_field_types = {'pose': 'Pose', 'covariance': 'float64'}

    def __init__(self, pose=None, covariance=None):
        self['pose'] = {} if pose is None else pose
        self['covariance'] = [] if covariance is None else covariance

dataMap = PoseWithCovariance.get_data_map()
