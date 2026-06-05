from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GetState_Response(Message):
    _TYPE_NAME = 'GetState_Response'
    _TYPE_DEF = _TYPE_DEFS['GetState_Response']
    _fields_and_field_types = {'current_state': 'State'}

    def __init__(self, current_state=None):
        self['current_state'] = {} if current_state is None else current_state

dataMap = GetState_Response.get_data_map()
