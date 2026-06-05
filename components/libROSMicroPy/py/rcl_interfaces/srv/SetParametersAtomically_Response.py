from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class SetParametersAtomically_Response(Message):
    _TYPE_NAME = 'SetParametersAtomically_Response'
    _TYPE_DEF = _TYPE_DEFS['SetParametersAtomically_Response']
    _fields_and_field_types = {'result': 'SetParametersResult'}

    def __init__(self, result=None):
        self['result'] = {} if result is None else result

dataMap = SetParametersAtomically_Response.get_data_map()
