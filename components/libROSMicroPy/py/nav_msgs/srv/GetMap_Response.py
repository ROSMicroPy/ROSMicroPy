from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GetMap_Response(Message):
    _TYPE_NAME = 'GetMap_Response'
    _TYPE_DEF = _TYPE_DEFS['GetMap_Response']
    _fields_and_field_types = {'map': 'OccupancyGrid'}

    def __init__(self, map=None):
        self['map'] = {} if map is None else map

dataMap = GetMap_Response.get_data_map()
