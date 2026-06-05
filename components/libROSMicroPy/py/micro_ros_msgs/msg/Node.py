from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Node(Message):
    _TYPE_NAME = 'Node'
    _TYPE_DEF = _TYPE_DEFS['Node']
    _fields_and_field_types = {'entities': 'Entity'}

    def __init__(self, entities=None):
        self['entities'] = [] if entities is None else entities

dataMap = Node.get_data_map()
