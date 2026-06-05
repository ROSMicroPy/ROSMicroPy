from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Builtins(Message):
    _TYPE_NAME = 'Builtins'
    _TYPE_DEF = _TYPE_DEFS['Builtins']
    _fields_and_field_types = {'duration_value': 'Duration', 'time_value': 'Time'}

    def __init__(self, duration_value=None, time_value=None):
        self['duration_value'] = {} if duration_value is None else duration_value
        self['time_value'] = {} if time_value is None else time_value

dataMap = Builtins.get_data_map()
