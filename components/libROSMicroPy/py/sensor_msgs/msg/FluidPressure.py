from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class FluidPressure(Message):
    _TYPE_NAME = 'FluidPressure'
    _TYPE_DEF = _TYPE_DEFS['FluidPressure']
    _fields_and_field_types = {'header': 'Header', 'fluid_pressure': 'float64', 'variance': 'float64'}

    def __init__(self, header=None, fluid_pressure=None, variance=None):
        self['header'] = {} if header is None else header
        self['fluid_pressure'] = 0.0 if fluid_pressure is None else fluid_pressure
        self['variance'] = 0.0 if variance is None else variance

dataMap = FluidPressure.get_data_map()
