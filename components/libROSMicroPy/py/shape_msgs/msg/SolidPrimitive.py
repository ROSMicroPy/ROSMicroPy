from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class SolidPrimitive(Message):
    _TYPE_NAME = 'SolidPrimitive'
    _TYPE_DEF = _TYPE_DEFS['SolidPrimitive']
    _fields_and_field_types = {'type': 'uint8', 'polygon': 'Polygon'}
    BOX = 1
    SPHERE = 2
    CYLINDER = 3
    CONE = 4
    PRISM = 5
    BOX_X = 0
    BOX_Y = 1
    BOX_Z = 2
    SPHERE_RADIUS = 0
    CYLINDER_HEIGHT = 0
    CYLINDER_RADIUS = 1
    CONE_HEIGHT = 0
    CONE_RADIUS = 1
    PRISM_HEIGHT = 0

    def __init__(self, type=None, polygon=None):
        self['type'] = 0 if type is None else type
        self['polygon'] = {} if polygon is None else polygon

dataMap = SolidPrimitive.get_data_map()
