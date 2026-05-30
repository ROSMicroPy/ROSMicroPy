from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class PolygonInstance(Message):
    _TYPE_NAME = 'PolygonInstance'
    _TYPE_DEF = _TYPE_DEFS['PolygonInstance']
    _fields_and_field_types = {'polygon': 'Polygon', 'id': 'int64'}

    def __init__(self, polygon=None, id=None):
        self['polygon'] = {} if polygon is None else polygon
        self['id'] = 0 if id is None else id

dataMap = PolygonInstance.get_data_map()
