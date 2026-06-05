from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class SetLoggerLevels_Request(Message):
    _TYPE_NAME = 'SetLoggerLevels_Request'
    _TYPE_DEF = _TYPE_DEFS['SetLoggerLevels_Request']
    _fields_and_field_types = {'levels': 'LoggerLevel'}

    def __init__(self, levels=None):
        self['levels'] = [] if levels is None else levels

dataMap = SetLoggerLevels_Request.get_data_map()
