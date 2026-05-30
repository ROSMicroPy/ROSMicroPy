from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class MultiArrayLayout(Message):
    _TYPE_NAME = 'MultiArrayLayout'
    _TYPE_DEF = _TYPE_DEFS['MultiArrayLayout']
    _fields_and_field_types = {'dim': 'MultiArrayDimension', 'data_offset': 'uint32'}

    def __init__(self, dim=None, data_offset=None):
        self['dim'] = [] if dim is None else dim
        self['data_offset'] = 0 if data_offset is None else data_offset

dataMap = MultiArrayLayout.get_data_map()
