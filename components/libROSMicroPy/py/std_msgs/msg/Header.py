from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Header(Message):
    _TYPE_NAME = 'Header'
    _TYPE_DEF = _TYPE_DEFS['Header']
    _fields_and_field_types = {'stamp': 'Time', 'frame_id': 'string'}

    def __init__(self, stamp=None, frame_id=None):
        self['stamp'] = {} if stamp is None else stamp
        self['frame_id'] = '' if frame_id is None else frame_id

dataMap = Header.get_data_map()
