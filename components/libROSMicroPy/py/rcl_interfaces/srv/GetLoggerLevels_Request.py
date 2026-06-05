from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GetLoggerLevels_Request(Message):
    _TYPE_NAME = 'GetLoggerLevels_Request'
    _TYPE_DEF = _TYPE_DEFS['GetLoggerLevels_Request']
    _fields_and_field_types = {'names': 'string'}

    def __init__(self, names=None):
        self['names'] = [] if names is None else names

dataMap = GetLoggerLevels_Request.get_data_map()
