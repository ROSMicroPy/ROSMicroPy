from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Temperature(Message):
    _TYPE_NAME = 'Temperature'
    _TYPE_DEF = _TYPE_DEFS['Temperature']
    _fields_and_field_types = {'header': 'Header', 'temperature': 'float64', 'variance': 'float64'}

    def __init__(self, header=None, temperature=None, variance=None):
        self['header'] = {} if header is None else header
        self['temperature'] = 0.0 if temperature is None else temperature
        self['variance'] = 0.0 if variance is None else variance

dataMap = Temperature.get_data_map()
