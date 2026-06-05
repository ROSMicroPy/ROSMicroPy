from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GoalStatus(Message):
    _TYPE_NAME = 'GoalStatus'
    _TYPE_DEF = _TYPE_DEFS['GoalStatus']
    _fields_and_field_types = {'goal_id': 'GoalID', 'status': 'uint8', 'text': 'string'}
    PENDING = 0
    ACTIVE = 1
    PREEMPTED = 2
    SUCCEEDED = 3
    ABORTED = 4
    REJECTED = 5
    PREEMPTING = 6
    RECALLING = 7
    RECALLED = 8
    LOST = 9

    def __init__(self, goal_id=None, status=None, text=None):
        self['goal_id'] = {} if goal_id is None else goal_id
        self['status'] = 0 if status is None else status
        self['text'] = '' if text is None else text

dataMap = GoalStatus.get_data_map()
