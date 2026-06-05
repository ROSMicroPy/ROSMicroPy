from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class ListParameters_Request(Message):
    _TYPE_NAME = 'ListParameters_Request'
    _TYPE_DEF = _TYPE_DEFS['ListParameters_Request']
    _fields_and_field_types = {'prefixes': 'string', 'depth': 'uint64'}
    DEPTH_RECURSIVE = 0

    def __init__(self, prefixes=None, depth=None):
        self['prefixes'] = [] if prefixes is None else prefixes
        self['depth'] = 0 if depth is None else depth

dataMap = ListParameters_Request.get_data_map()
