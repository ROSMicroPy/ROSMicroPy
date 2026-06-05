from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class ListParameters_Response(Message):
    _TYPE_NAME = 'ListParameters_Response'
    _TYPE_DEF = _TYPE_DEFS['ListParameters_Response']
    _fields_and_field_types = {'result': 'ListParametersResult'}

    def __init__(self, result=None):
        self['result'] = {} if result is None else result

dataMap = ListParameters_Response.get_data_map()
