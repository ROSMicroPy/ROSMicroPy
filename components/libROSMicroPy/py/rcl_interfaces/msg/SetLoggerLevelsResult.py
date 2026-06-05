from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class SetLoggerLevelsResult(Message):
    _TYPE_NAME = 'SetLoggerLevelsResult'
    _TYPE_DEF = _TYPE_DEFS['SetLoggerLevelsResult']
    _fields_and_field_types = {'successful': 'bool', 'reason': 'string'}

    def __init__(self, successful=None, reason=None):
        self['successful'] = False if successful is None else successful
        self['reason'] = '' if reason is None else reason

dataMap = SetLoggerLevelsResult.get_data_map()
