from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class InteractiveMarkerUpdate(Message):
    _TYPE_NAME = 'InteractiveMarkerUpdate'
    _TYPE_DEF = _TYPE_DEFS['InteractiveMarkerUpdate']
    _fields_and_field_types = {'server_id': 'string', 'seq_num': 'uint64', 'type': 'uint8', 'markers': 'InteractiveMarker', 'poses': 'InteractiveMarkerPose', 'erases': 'string'}
    KEEP_ALIVE = 0
    UPDATE = 1

    def __init__(self, server_id=None, seq_num=None, type=None, markers=None, poses=None, erases=None):
        self['server_id'] = '' if server_id is None else server_id
        self['seq_num'] = 0 if seq_num is None else seq_num
        self['type'] = 0 if type is None else type
        self['markers'] = [] if markers is None else markers
        self['poses'] = [] if poses is None else poses
        self['erases'] = [] if erases is None else erases

dataMap = InteractiveMarkerUpdate.get_data_map()
