from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class PolygonInstanceStamped(Message):
    _TYPE_NAME = 'PolygonInstanceStamped'
    _TYPE_DEF = _TYPE_DEFS['PolygonInstanceStamped']
    _fields_and_field_types = {'header': 'Header', 'polygon': 'PolygonInstance'}

    def __init__(self, header=None, polygon=None):
        self['header'] = {} if header is None else header
        self['polygon'] = {} if polygon is None else polygon

dataMap = PolygonInstanceStamped.get_data_map()
