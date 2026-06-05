from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class State(Message):
    _TYPE_NAME = 'State'
    _TYPE_DEF = _TYPE_DEFS['State']
    _fields_and_field_types = {'id': 'uint8', 'label': 'string'}
    PRIMARY_STATE_UNKNOWN = 0
    PRIMARY_STATE_UNCONFIGURED = 1
    PRIMARY_STATE_INACTIVE = 2
    PRIMARY_STATE_ACTIVE = 3
    PRIMARY_STATE_FINALIZED = 4
    TRANSITION_STATE_CONFIGURING = 10
    TRANSITION_STATE_CLEANINGUP = 11
    TRANSITION_STATE_SHUTTINGDOWN = 12
    TRANSITION_STATE_ACTIVATING = 13
    TRANSITION_STATE_DEACTIVATING = 14
    TRANSITION_STATE_ERRORPROCESSING = 15

    def __init__(self, id=None, label=None):
        self['id'] = 0 if id is None else id
        self['label'] = '' if label is None else label

dataMap = State.get_data_map()
