from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Path(Message):
    _TYPE_NAME = 'Path'
    _TYPE_DEF = _TYPE_DEFS['Path']
    _fields_and_field_types = {'header': 'Header', 'poses': 'PoseStamped'}

    def __init__(self, header=None, poses=None):
        self['header'] = {} if header is None else header
        self['poses'] = [] if poses is None else poses

dataMap = Path.get_data_map()
