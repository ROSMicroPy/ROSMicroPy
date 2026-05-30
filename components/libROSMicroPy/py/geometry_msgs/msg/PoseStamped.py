from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class PoseStamped(Message):
    _TYPE_NAME = 'PoseStamped'
    _TYPE_DEF = _TYPE_DEFS['PoseStamped']
    _fields_and_field_types = {'header': 'Header', 'pose': 'Pose'}

    def __init__(self, header=None, pose=None):
        self['header'] = {} if header is None else header
        self['pose'] = {} if pose is None else pose

dataMap = PoseStamped.get_data_map()
