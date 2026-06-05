from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Topic(Message):
    _TYPE_NAME = 'Topic'
    _TYPE_DEF = _TYPE_DEFS['Topic']
    _fields_and_field_types = {'name': 'string', 'type': 'InterfaceType', 'qos': 'QoSProfile'}

    def __init__(self, name=None, type=None, qos=None):
        self['name'] = '' if name is None else name
        self['type'] = {} if type is None else type
        self['qos'] = {} if qos is None else qos

dataMap = Topic.get_data_map()
