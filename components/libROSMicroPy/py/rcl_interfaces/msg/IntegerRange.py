from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class IntegerRange(Message):
    _TYPE_NAME = 'IntegerRange'
    _TYPE_DEF = _TYPE_DEFS['IntegerRange']
    _fields_and_field_types = {'from_value': 'int64', 'to_value': 'int64', 'step': 'uint64'}

    def __init__(self, from_value=None, to_value=None, step=None):
        self['from_value'] = 0 if from_value is None else from_value
        self['to_value'] = 0 if to_value is None else to_value
        self['step'] = 0 if step is None else step

dataMap = IntegerRange.get_data_map()
