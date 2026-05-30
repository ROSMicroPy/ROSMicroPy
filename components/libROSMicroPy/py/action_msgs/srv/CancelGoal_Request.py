from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class CancelGoal_Request(Message):
    _TYPE_NAME = 'CancelGoal_Request'
    _TYPE_DEF = _TYPE_DEFS['CancelGoal_Request']
    _fields_and_field_types = {'goal_info': 'GoalInfo'}

    def __init__(self, goal_info=None):
        self['goal_info'] = {} if goal_info is None else goal_info

dataMap = CancelGoal_Request.get_data_map()
