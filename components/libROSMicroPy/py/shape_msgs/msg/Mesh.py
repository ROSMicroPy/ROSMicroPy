from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Mesh(Message):
    _TYPE_NAME = 'Mesh'
    _TYPE_DEF = _TYPE_DEFS['Mesh']
    _fields_and_field_types = {'triangles': 'MeshTriangle', 'vertices': 'Point'}

    def __init__(self, triangles=None, vertices=None):
        self['triangles'] = [] if triangles is None else triangles
        self['vertices'] = [] if vertices is None else vertices

dataMap = Mesh.get_data_map()
