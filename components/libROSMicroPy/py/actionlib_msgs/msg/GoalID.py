from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GoalID(Message):
    _TYPE_NAME = 'GoalID'
    _TYPE_DEF = _TYPE_DEFS['GoalID']
    _fields_and_field_types = {'stamp': 'Time', 'id': 'string'}

    def __init__(self, stamp=None, id=None):
        self['stamp'] = {} if stamp is None else stamp
        self['id'] = '' if id is None else id

dataMap = GoalID.get_data_map()
