from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class UInt8MultiArray(Message):
    _TYPE_NAME = 'UInt8MultiArray'
    _TYPE_DEF = _TYPE_DEFS['UInt8MultiArray']
    _fields_and_field_types = {'layout': 'MultiArrayLayout', 'data': 'uint8'}

    def __init__(self, layout=None, data=None):
        self['layout'] = {} if layout is None else layout
        self['data'] = [] if data is None else data

dataMap = UInt8MultiArray.get_data_map()
