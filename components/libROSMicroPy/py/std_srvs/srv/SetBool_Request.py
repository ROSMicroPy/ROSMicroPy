from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class SetBool_Request(Message):
    _TYPE_NAME = 'SetBool_Request'
    _TYPE_DEF = _TYPE_DEFS['SetBool_Request']
    _fields_and_field_types = {'data': 'bool'}

    def __init__(self, data=None):
        self['data'] = False if data is None else data

dataMap = SetBool_Request.get_data_map()
