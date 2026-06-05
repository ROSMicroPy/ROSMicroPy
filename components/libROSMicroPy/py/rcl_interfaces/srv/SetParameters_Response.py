from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class SetParameters_Response(Message):
    _TYPE_NAME = 'SetParameters_Response'
    _TYPE_DEF = _TYPE_DEFS['SetParameters_Response']
    _fields_and_field_types = {'results': 'SetParametersResult'}

    def __init__(self, results=None):
        self['results'] = [] if results is None else results

dataMap = SetParameters_Response.get_data_map()
