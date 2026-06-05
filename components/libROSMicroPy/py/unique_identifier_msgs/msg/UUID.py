from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class UUID(Message):
    _TYPE_NAME = 'UUID'
    _TYPE_DEF = _TYPE_DEFS['UUID']
    _fields_and_field_types = {'uuid': 'uint8'}

    def __init__(self, uuid=None):
        self['uuid'] = [] if uuid is None else uuid

dataMap = UUID.get_data_map()
