from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class ChangeState_Request(Message):
    _TYPE_NAME = 'ChangeState_Request'
    _TYPE_DEF = _TYPE_DEFS['ChangeState_Request']
    _fields_and_field_types = {'transition': 'Transition'}

    def __init__(self, transition=None):
        self['transition'] = {} if transition is None else transition

dataMap = ChangeState_Request.get_data_map()
