from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class LoggerLevel(Message):
    _TYPE_NAME = 'LoggerLevel'
    _TYPE_DEF = _TYPE_DEFS['LoggerLevel']
    _fields_and_field_types = {'name': 'string', 'level': 'uint32'}
    LOG_LEVEL_UNKNOWN = 0
    LOG_LEVEL_DEBUG = 10
    LOG_LEVEL_INFO = 20
    LOG_LEVEL_WARN = 30
    LOG_LEVEL_ERROR = 40
    LOG_LEVEL_FATAL = 50

    def __init__(self, name=None, level=None):
        self['name'] = '' if name is None else name
        self['level'] = 0 if level is None else level

dataMap = LoggerLevel.get_data_map()
