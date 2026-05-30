from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class MeshTriangle(Message):
    _TYPE_NAME = 'MeshTriangle'
    _TYPE_DEF = _TYPE_DEFS['MeshTriangle']
    _fields_and_field_types = {'vertex_indices': 'uint32'}

    def __init__(self, vertex_indices=None):
        self['vertex_indices'] = [] if vertex_indices is None else vertex_indices

dataMap = MeshTriangle.get_data_map()
