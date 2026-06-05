from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class SetLoggerLevels_Response(Message):
    _TYPE_NAME = 'SetLoggerLevels_Response'
    _TYPE_DEF = _TYPE_DEFS['SetLoggerLevels_Response']
    _fields_and_field_types = {'results': 'SetLoggerLevelsResult'}

    def __init__(self, results=None):
        self['results'] = [] if results is None else results

dataMap = SetLoggerLevels_Response.get_data_map()
