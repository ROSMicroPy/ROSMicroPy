from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class UnloadNode_Response(Message):
    _TYPE_NAME = 'UnloadNode_Response'
    _TYPE_DEF = _TYPE_DEFS['UnloadNode_Response']
    _fields_and_field_types = {'success': 'bool', 'error_message': 'string'}

    def __init__(self, success=None, error_message=None):
        self['success'] = False if success is None else success
        self['error_message'] = '' if error_message is None else error_message

dataMap = UnloadNode_Response.get_data_map()
