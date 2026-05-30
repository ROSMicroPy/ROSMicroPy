from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Illuminance(Message):
    _TYPE_NAME = 'Illuminance'
    _TYPE_DEF = _TYPE_DEFS['Illuminance']
    _fields_and_field_types = {'header': 'Header', 'illuminance': 'float64', 'variance': 'float64'}

    def __init__(self, header=None, illuminance=None, variance=None):
        self['header'] = {} if header is None else header
        self['illuminance'] = 0.0 if illuminance is None else illuminance
        self['variance'] = 0.0 if variance is None else variance

dataMap = Illuminance.get_data_map()
