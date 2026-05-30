from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class RelativeHumidity(Message):
    _TYPE_NAME = 'RelativeHumidity'
    _TYPE_DEF = _TYPE_DEFS['RelativeHumidity']
    _fields_and_field_types = {'header': 'Header', 'relative_humidity': 'float64', 'variance': 'float64'}

    def __init__(self, header=None, relative_humidity=None, variance=None):
        self['header'] = {} if header is None else header
        self['relative_humidity'] = 0.0 if relative_humidity is None else relative_humidity
        self['variance'] = 0.0 if variance is None else variance

dataMap = RelativeHumidity.get_data_map()
