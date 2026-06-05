from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GoalStatusArray(Message):
    _TYPE_NAME = 'GoalStatusArray'
    _TYPE_DEF = _TYPE_DEFS['GoalStatusArray']
    _fields_and_field_types = {'header': 'Header', 'status_list': 'GoalStatus'}

    def __init__(self, header=None, status_list=None):
        self['header'] = {} if header is None else header
        self['status_list'] = [] if status_list is None else status_list

dataMap = GoalStatusArray.get_data_map()
