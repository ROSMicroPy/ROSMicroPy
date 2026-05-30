from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GoalStatus(Message):
    _TYPE_NAME = 'GoalStatus'
    _TYPE_DEF = _TYPE_DEFS['GoalStatus']
    _fields_and_field_types = {'goal_info': 'GoalInfo', 'status': 'int8'}
    STATUS_UNKNOWN = 0
    STATUS_ACCEPTED = 1
    STATUS_EXECUTING = 2
    STATUS_CANCELING = 3
    STATUS_SUCCEEDED = 4
    STATUS_CANCELED = 5
    STATUS_ABORTED = 6

    def __init__(self, goal_info=None, status=None):
        self['goal_info'] = {} if goal_info is None else goal_info
        self['status'] = 0 if status is None else status

dataMap = GoalStatus.get_data_map()
