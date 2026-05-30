from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class PoseWithCovarianceStamped(Message):
    _TYPE_NAME = 'PoseWithCovarianceStamped'
    _TYPE_DEF = _TYPE_DEFS['PoseWithCovarianceStamped']
    _fields_and_field_types = {'header': 'Header', 'pose': 'PoseWithCovariance'}

    def __init__(self, header=None, pose=None):
        self['header'] = {} if header is None else header
        self['pose'] = {} if pose is None else pose

dataMap = PoseWithCovarianceStamped.get_data_map()
