from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class SetParametersAtomically_Request(Message):
    _TYPE_NAME = 'SetParametersAtomically_Request'
    _TYPE_DEF = _TYPE_DEFS['SetParametersAtomically_Request']
    _fields_and_field_types = {'parameters': 'Parameter'}

    def __init__(self, parameters=None):
        self['parameters'] = [] if parameters is None else parameters

dataMap = SetParametersAtomically_Request.get_data_map()
