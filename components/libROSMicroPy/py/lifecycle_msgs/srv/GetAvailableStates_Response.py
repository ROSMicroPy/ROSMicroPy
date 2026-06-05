from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GetAvailableStates_Response(Message):
    _TYPE_NAME = 'GetAvailableStates_Response'
    _TYPE_DEF = _TYPE_DEFS['GetAvailableStates_Response']
    _fields_and_field_types = {'available_states': 'State'}

    def __init__(self, available_states=None):
        self['available_states'] = [] if available_states is None else available_states

dataMap = GetAvailableStates_Response.get_data_map()
