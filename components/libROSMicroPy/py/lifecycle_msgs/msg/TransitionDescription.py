from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class TransitionDescription(Message):
    _TYPE_NAME = 'TransitionDescription'
    _TYPE_DEF = _TYPE_DEFS['TransitionDescription']
    _fields_and_field_types = {'transition': 'Transition', 'start_state': 'State', 'goal_state': 'State'}

    def __init__(self, transition=None, start_state=None, goal_state=None):
        self['transition'] = {} if transition is None else transition
        self['start_state'] = {} if start_state is None else start_state
        self['goal_state'] = {} if goal_state is None else goal_state

dataMap = TransitionDescription.get_data_map()
