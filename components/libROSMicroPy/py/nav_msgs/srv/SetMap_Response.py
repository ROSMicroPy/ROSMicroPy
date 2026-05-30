from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class SetMap_Response(Message):
    _TYPE_NAME = 'SetMap_Response'
    _TYPE_DEF = _TYPE_DEFS['SetMap_Response']
    _fields_and_field_types = {'success': 'bool'}

    def __init__(self, success=None):
        self['success'] = False if success is None else success

dataMap = SetMap_Response.get_data_map()
