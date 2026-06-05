from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class FloatingPointRange(Message):
    _TYPE_NAME = 'FloatingPointRange'
    _TYPE_DEF = _TYPE_DEFS['FloatingPointRange']
    _fields_and_field_types = {'from_value': 'float64', 'to_value': 'float64', 'step': 'float64'}

    def __init__(self, from_value=None, to_value=None, step=None):
        self['from_value'] = 0.0 if from_value is None else from_value
        self['to_value'] = 0.0 if to_value is None else to_value
        self['step'] = 0.0 if step is None else step

dataMap = FloatingPointRange.get_data_map()
