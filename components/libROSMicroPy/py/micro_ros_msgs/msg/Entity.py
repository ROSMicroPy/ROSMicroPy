from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Entity(Message):
    _TYPE_NAME = 'Entity'
    _TYPE_DEF = _TYPE_DEFS['Entity']
    _fields_and_field_types = {'entity_type': 'byte'}
    PUBLISHER = 0
    SUBSCRIBER = 1
    SERVICE_SERVER = 2
    SERVICE_CLIENT = 3

    def __init__(self, entity_type=None):
        self['entity_type'] = 0 if entity_type is None else entity_type

dataMap = Entity.get_data_map()
