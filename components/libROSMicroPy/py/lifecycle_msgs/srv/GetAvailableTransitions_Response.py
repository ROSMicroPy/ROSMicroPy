from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GetAvailableTransitions_Response(Message):
    _TYPE_NAME = 'GetAvailableTransitions_Response'
    _TYPE_DEF = _TYPE_DEFS['GetAvailableTransitions_Response']
    _fields_and_field_types = {'available_transitions': 'TransitionDescription'}

    def __init__(self, available_transitions=None):
        self['available_transitions'] = [] if available_transitions is None else available_transitions

dataMap = GetAvailableTransitions_Response.get_data_map()
