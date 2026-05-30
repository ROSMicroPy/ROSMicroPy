from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class PoseArray(Message):
    _TYPE_NAME = 'PoseArray'
    _TYPE_DEF = _TYPE_DEFS['PoseArray']
    _fields_and_field_types = {'header': 'Header', 'poses': 'Pose'}

    def __init__(self, header=None, poses=None):
        self['header'] = {} if header is None else header
        self['poses'] = [] if poses is None else poses

dataMap = PoseArray.get_data_map()
