from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Plane(Message):
    _TYPE_NAME = 'Plane'
    _TYPE_DEF = _TYPE_DEFS['Plane']
    _fields_and_field_types = {'coef': 'float64'}

    def __init__(self, coef=None):
        self['coef'] = [] if coef is None else coef

dataMap = Plane.get_data_map()
