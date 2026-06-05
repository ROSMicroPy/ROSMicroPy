from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GetParameterTypes_Response(Message):
    _TYPE_NAME = 'GetParameterTypes_Response'
    _TYPE_DEF = _TYPE_DEFS['GetParameterTypes_Response']
    _fields_and_field_types = {'types': 'uint8'}

    def __init__(self, types=None):
        self['types'] = [] if types is None else types

dataMap = GetParameterTypes_Response.get_data_map()
