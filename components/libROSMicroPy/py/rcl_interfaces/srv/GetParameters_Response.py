from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GetParameters_Response(Message):
    _TYPE_NAME = 'GetParameters_Response'
    _TYPE_DEF = _TYPE_DEFS['GetParameters_Response']
    _fields_and_field_types = {'values': 'ParameterValue'}

    def __init__(self, values=None):
        self['values'] = [] if values is None else values

dataMap = GetParameters_Response.get_data_map()
