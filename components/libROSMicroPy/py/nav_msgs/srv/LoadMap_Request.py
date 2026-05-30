from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class LoadMap_Request(Message):
    _TYPE_NAME = 'LoadMap_Request'
    _TYPE_DEF = _TYPE_DEFS['LoadMap_Request']
    _fields_and_field_types = {'map_url': 'string'}

    def __init__(self, map_url=None):
        self['map_url'] = '' if map_url is None else map_url

dataMap = LoadMap_Request.get_data_map()
