from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class LoadMap_Response(Message):
    _TYPE_NAME = 'LoadMap_Response'
    _TYPE_DEF = _TYPE_DEFS['LoadMap_Response']
    _fields_and_field_types = {'map': 'OccupancyGrid', 'result': 'uint8'}
    RESULT_SUCCESS = 0
    RESULT_MAP_DOES_NOT_EXIST = 1
    RESULT_INVALID_MAP_DATA = 2
    RESULT_INVALID_MAP_METADATA = 3
    RESULT_UNDEFINED_FAILURE = 255

    def __init__(self, map=None, result=None):
        self['map'] = {} if map is None else map
        self['result'] = 0 if result is None else result

dataMap = LoadMap_Response.get_data_map()
