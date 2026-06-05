from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Float32MultiArray(Message):
    _TYPE_NAME = 'Float32MultiArray'
    _TYPE_DEF = _TYPE_DEFS['Float32MultiArray']
    _fields_and_field_types = {'layout': 'MultiArrayLayout', 'data': 'float32'}

    def __init__(self, layout=None, data=None):
        self['layout'] = {} if layout is None else layout
        self['data'] = [] if data is None else data

dataMap = Float32MultiArray.get_data_map()
