from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Graph(Message):
    _TYPE_NAME = 'Graph'
    _TYPE_DEF = _TYPE_DEFS['Graph']
    _fields_and_field_types = {'nodes': 'Node'}

    def __init__(self, nodes=None):
        self['nodes'] = [] if nodes is None else nodes

dataMap = Graph.get_data_map()
