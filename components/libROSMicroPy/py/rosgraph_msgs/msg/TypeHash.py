from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class TypeHash(Message):
    _TYPE_NAME = 'TypeHash'
    _TYPE_DEF = _TYPE_DEFS['TypeHash']
    _fields_and_field_types = {'version': 'uint8', 'value': 'uint8'}

    def __init__(self, version=None, value=None):
        self['version'] = 0 if version is None else version
        self['value'] = [] if value is None else value

dataMap = TypeHash.get_data_map()
