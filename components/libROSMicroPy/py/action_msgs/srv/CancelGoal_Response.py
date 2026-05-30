from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class CancelGoal_Response(Message):
    _TYPE_NAME = 'CancelGoal_Response'
    _TYPE_DEF = _TYPE_DEFS['CancelGoal_Response']
    _fields_and_field_types = {'return_code': 'int8', 'goals_canceling': 'GoalInfo'}
    ERROR_NONE = 0
    ERROR_REJECTED = 1
    ERROR_UNKNOWN_GOAL_ID = 2
    ERROR_GOAL_TERMINATED = 3

    def __init__(self, return_code=None, goals_canceling=None):
        self['return_code'] = 0 if return_code is None else return_code
        self['goals_canceling'] = [] if goals_canceling is None else goals_canceling

dataMap = CancelGoal_Response.get_data_map()
