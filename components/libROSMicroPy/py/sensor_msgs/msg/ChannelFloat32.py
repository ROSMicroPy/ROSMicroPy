from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class ChannelFloat32(Message):
    _TYPE_NAME = 'ChannelFloat32'
    _TYPE_DEF = _TYPE_DEFS['ChannelFloat32']
    _fields_and_field_types = {'name': 'string', 'values': 'float32'}

    def __init__(self, name=None, values=None):
        self['name'] = '' if name is None else name
        self['values'] = [] if values is None else values

dataMap = ChannelFloat32.get_data_map()
