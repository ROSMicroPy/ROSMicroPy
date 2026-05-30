from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Goals(Message):
    _TYPE_NAME = 'Goals'
    _TYPE_DEF = _TYPE_DEFS['Goals']
    _fields_and_field_types = {'header': 'Header', 'goals': 'PoseStamped'}

    def __init__(self, header=None, goals=None):
        self['header'] = {} if header is None else header
        self['goals'] = [] if goals is None else goals

dataMap = Goals.get_data_map()
