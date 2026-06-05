from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class SetParameters_Request(Message):
    _TYPE_NAME = 'SetParameters_Request'
    _TYPE_DEF = _TYPE_DEFS['SetParameters_Request']
    _fields_and_field_types = {'parameters': 'Parameter'}

    def __init__(self, parameters=None):
        self['parameters'] = [] if parameters is None else parameters

dataMap = SetParameters_Request.get_data_map()
