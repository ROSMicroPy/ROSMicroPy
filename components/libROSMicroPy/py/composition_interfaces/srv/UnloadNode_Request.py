from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class UnloadNode_Request(Message):
    _TYPE_NAME = 'UnloadNode_Request'
    _TYPE_DEF = _TYPE_DEFS['UnloadNode_Request']
    _fields_and_field_types = {'unique_id': 'uint64'}

    def __init__(self, unique_id=None):
        self['unique_id'] = 0 if unique_id is None else unique_id

dataMap = UnloadNode_Request.get_data_map()
