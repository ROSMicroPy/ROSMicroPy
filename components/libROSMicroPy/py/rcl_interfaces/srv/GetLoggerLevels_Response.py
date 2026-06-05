from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GetLoggerLevels_Response(Message):
    _TYPE_NAME = 'GetLoggerLevels_Response'
    _TYPE_DEF = _TYPE_DEFS['GetLoggerLevels_Response']
    _fields_and_field_types = {'levels': 'LoggerLevel'}

    def __init__(self, levels=None):
        self['levels'] = [] if levels is None else levels

dataMap = GetLoggerLevels_Response.get_data_map()
