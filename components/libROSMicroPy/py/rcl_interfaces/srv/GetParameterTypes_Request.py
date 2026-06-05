from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GetParameterTypes_Request(Message):
    _TYPE_NAME = 'GetParameterTypes_Request'
    _TYPE_DEF = _TYPE_DEFS['GetParameterTypes_Request']
    _fields_and_field_types = {'names': 'string'}

    def __init__(self, names=None):
        self['names'] = [] if names is None else names

dataMap = GetParameterTypes_Request.get_data_map()
