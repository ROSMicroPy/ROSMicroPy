from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Int64MultiArray(Message):
    _TYPE_NAME = 'Int64MultiArray'
    _TYPE_DEF = _TYPE_DEFS['Int64MultiArray']
    _fields_and_field_types = {'layout': 'MultiArrayLayout', 'data': 'int64'}

    def __init__(self, layout=None, data=None):
        self['layout'] = {} if layout is None else layout
        self['data'] = [] if data is None else data

dataMap = Int64MultiArray.get_data_map()
