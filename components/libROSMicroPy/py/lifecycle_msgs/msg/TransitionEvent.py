from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class TransitionEvent(Message):
    _TYPE_NAME = 'TransitionEvent'
    _TYPE_DEF = _TYPE_DEFS['TransitionEvent']
    _fields_and_field_types = {'timestamp': 'uint64', 'transition': 'Transition', 'start_state': 'State', 'goal_state': 'State'}

    def __init__(self, timestamp=None, transition=None, start_state=None, goal_state=None):
        self['timestamp'] = 0 if timestamp is None else timestamp
        self['transition'] = {} if transition is None else transition
        self['start_state'] = {} if start_state is None else start_state
        self['goal_state'] = {} if goal_state is None else goal_state

dataMap = TransitionEvent.get_data_map()
