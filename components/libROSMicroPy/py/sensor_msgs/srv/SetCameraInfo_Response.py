from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class SetCameraInfo_Response(Message):
    _TYPE_NAME = 'SetCameraInfo_Response'
    _TYPE_DEF = _TYPE_DEFS['SetCameraInfo_Response']
    _fields_and_field_types = {'success': 'bool', 'status_message': 'string'}

    def __init__(self, success=None, status_message=None):
        self['success'] = False if success is None else success
        self['status_message'] = '' if status_message is None else status_message

dataMap = SetCameraInfo_Response.get_data_map()
