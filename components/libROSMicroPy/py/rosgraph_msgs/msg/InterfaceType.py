from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class InterfaceType(Message):
    _TYPE_NAME = 'InterfaceType'
    _TYPE_DEF = _TYPE_DEFS['InterfaceType']
    _fields_and_field_types = {'name': 'string', 'hash': 'TypeHash'}

    def __init__(self, name=None, hash=None):
        self['name'] = '' if name is None else name
        self['hash'] = {} if hash is None else hash

dataMap = InterfaceType.get_data_map()
