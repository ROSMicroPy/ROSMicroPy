from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class InteractiveMarkerPose(Message):
    _TYPE_NAME = 'InteractiveMarkerPose'
    _TYPE_DEF = _TYPE_DEFS['InteractiveMarkerPose']
    _fields_and_field_types = {'header': 'Header', 'pose': 'Pose', 'name': 'string'}

    def __init__(self, header=None, pose=None, name=None):
        self['header'] = {} if header is None else header
        self['pose'] = {} if pose is None else pose
        self['name'] = '' if name is None else name

dataMap = InteractiveMarkerPose.get_data_map()
