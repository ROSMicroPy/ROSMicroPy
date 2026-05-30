from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GoalInfo(Message):
    _TYPE_NAME = 'GoalInfo'
    _TYPE_DEF = _TYPE_DEFS['GoalInfo']
    _fields_and_field_types = {'goal_id': 'UUID', 'stamp': 'Time'}

    def __init__(self, goal_id=None, stamp=None):
        self['goal_id'] = {} if goal_id is None else goal_id
        self['stamp'] = {} if stamp is None else stamp

dataMap = GoalInfo.get_data_map()
