from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class SetCameraInfo_Request(Message):
    _TYPE_NAME = 'SetCameraInfo_Request'
    _TYPE_DEF = _TYPE_DEFS['SetCameraInfo_Request']
    _fields_and_field_types = {'camera_info': 'CameraInfo'}

    def __init__(self, camera_info=None):
        self['camera_info'] = {} if camera_info is None else camera_info

dataMap = SetCameraInfo_Request.get_data_map()
