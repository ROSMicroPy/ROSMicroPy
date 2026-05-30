from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class SetMap_Request(Message):
    _TYPE_NAME = 'SetMap_Request'
    _TYPE_DEF = _TYPE_DEFS['SetMap_Request']
    _fields_and_field_types = {'map': 'OccupancyGrid', 'initial_pose': 'PoseWithCovarianceStamped'}

    def __init__(self, map=None, initial_pose=None):
        self['map'] = {} if map is None else map
        self['initial_pose'] = {} if initial_pose is None else initial_pose

dataMap = SetMap_Request.get_data_map()
