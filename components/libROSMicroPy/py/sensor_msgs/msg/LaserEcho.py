from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class LaserEcho(Message):
    _TYPE_NAME = 'LaserEcho'
    _TYPE_DEF = _TYPE_DEFS['LaserEcho']
    _fields_and_field_types = {'echoes': 'float32'}

    def __init__(self, echoes=None):
        self['echoes'] = [] if echoes is None else echoes

dataMap = LaserEcho.get_data_map()
