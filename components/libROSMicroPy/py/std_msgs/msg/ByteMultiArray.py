from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class ByteMultiArray(Message):
    _TYPE_NAME = 'ByteMultiArray'
    _TYPE_DEF = _TYPE_DEFS['ByteMultiArray']
    _fields_and_field_types = {'layout': 'MultiArrayLayout', 'data': 'byte'}

    def __init__(self, layout=None, data=None):
        self['layout'] = {} if layout is None else layout
        self['data'] = [] if data is None else data

dataMap = ByteMultiArray.get_data_map()
