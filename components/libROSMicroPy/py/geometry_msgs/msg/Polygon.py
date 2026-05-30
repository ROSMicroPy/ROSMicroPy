from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Polygon(Message):
    _TYPE_NAME = 'Polygon'
    _TYPE_DEF = _TYPE_DEFS['Polygon']
    _fields_and_field_types = {'points': 'Point32'}

    def __init__(self, points=None):
        self['points'] = [] if points is None else points

dataMap = Polygon.get_data_map()
