from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Int8MultiArray(Message):
    _TYPE_NAME = 'Int8MultiArray'
    _TYPE_DEF = _TYPE_DEFS['Int8MultiArray']
    _fields_and_field_types = {'layout': 'MultiArrayLayout', 'data': 'int8'}

    def __init__(self, layout=None, data=None):
        self['layout'] = {} if layout is None else layout
        self['data'] = [] if data is None else data

dataMap = Int8MultiArray.get_data_map()
