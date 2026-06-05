from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Clock(Message):
    _TYPE_NAME = 'Clock'
    _TYPE_DEF = _TYPE_DEFS['Clock']
    _fields_and_field_types = {'clock': 'Time'}

    def __init__(self, clock=None):
        self['clock'] = {} if clock is None else clock

dataMap = Clock.get_data_map()
