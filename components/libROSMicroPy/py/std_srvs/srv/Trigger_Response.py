from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Trigger_Response(Message):
    _TYPE_NAME = 'Trigger_Response'
    _TYPE_DEF = _TYPE_DEFS['Trigger_Response']
    _fields_and_field_types = {'success': 'bool', 'message': 'string'}

    def __init__(self, success=None, message=None):
        self['success'] = False if success is None else success
        self['message'] = '' if message is None else message

dataMap = Trigger_Response.get_data_map()
