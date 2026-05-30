from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class PolygonStamped(Message):
    _TYPE_NAME = 'PolygonStamped'
    _TYPE_DEF = _TYPE_DEFS['PolygonStamped']
    _fields_and_field_types = {'header': 'Header', 'polygon': 'Polygon'}

    def __init__(self, header=None, polygon=None):
        self['header'] = {} if header is None else header
        self['polygon'] = {} if polygon is None else polygon

dataMap = PolygonStamped.get_data_map()
