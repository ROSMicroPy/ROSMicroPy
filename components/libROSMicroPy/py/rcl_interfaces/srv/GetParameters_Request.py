from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GetParameters_Request(Message):
    _TYPE_NAME = 'GetParameters_Request'
    _TYPE_DEF = _TYPE_DEFS['GetParameters_Request']
    _fields_and_field_types = {'names': 'string'}

    def __init__(self, names=None):
        self['names'] = [] if names is None else names

dataMap = GetParameters_Request.get_data_map()
