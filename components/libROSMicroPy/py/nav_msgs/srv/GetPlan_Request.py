from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GetPlan_Request(Message):
    _TYPE_NAME = 'GetPlan_Request'
    _TYPE_DEF = _TYPE_DEFS['GetPlan_Request']
    _fields_and_field_types = {'start': 'PoseStamped', 'goal': 'PoseStamped', 'tolerance': 'float32'}

    def __init__(self, start=None, goal=None, tolerance=None):
        self['start'] = {} if start is None else start
        self['goal'] = {} if goal is None else goal
        self['tolerance'] = 0.0 if tolerance is None else tolerance

dataMap = GetPlan_Request.get_data_map()
