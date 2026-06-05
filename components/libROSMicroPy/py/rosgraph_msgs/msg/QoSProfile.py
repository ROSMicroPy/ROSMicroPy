from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class QoSProfile(Message):
    _TYPE_NAME = 'QoSProfile'
    _TYPE_DEF = _TYPE_DEFS['QoSProfile']
    _fields_and_field_types = {'depth': 'uint32', 'deadline': 'Duration', 'lifespan': 'Duration', 'history': 'uint8', 'reliability': 'uint8', 'durability': 'uint8', 'liveliness': 'uint8', 'liveliness_lease_duration': 'Duration'}
    HISTORY_SYSTEM_DEFAULT = 0
    HISTORY_KEEP_LAST = 1
    HISTORY_KEEP_ALL = 2
    HISTORY_UNKNOWN = 3
    RELIABILITY_SYSTEM_DEFAULT = 0
    RELIABILITY_RELIABLE = 1
    RELIABILITY_BEST_EFFORT = 2
    RELIABILITY_UNKNOWN = 3
    RELIABILITY_BEST_AVAILABLE = 4
    DURABILITY_SYSTEM_DEFAULT = 0
    DURABILITY_TRANSIENT_LOCAL = 1
    DURABILITY_VOLATILE = 2
    DURABILITY_UNKNOWN = 3
    DURABILITY_BEST_AVAILABLE = 4
    LIVELINESS_SYSTEM_DEFAULT = 0
    LIVELINESS_AUTOMATIC = 1
    LIVELINESS_MANUAL_BY_TOPIC = 3
    LIVELINESS_UNKNOWN = 4
    LIVELINESS_BEST_AVAILABLE = 5

    def __init__(self, depth=None, deadline=None, lifespan=None, history=None, reliability=None, durability=None, liveliness=None, liveliness_lease_duration=None):
        self['depth'] = 0 if depth is None else depth
        self['deadline'] = {} if deadline is None else deadline
        self['lifespan'] = {} if lifespan is None else lifespan
        self['history'] = 0 if history is None else history
        self['reliability'] = 0 if reliability is None else reliability
        self['durability'] = 0 if durability is None else durability
        self['liveliness'] = 0 if liveliness is None else liveliness
        self['liveliness_lease_duration'] = {} if liveliness_lease_duration is None else liveliness_lease_duration

dataMap = QoSProfile.get_data_map()
