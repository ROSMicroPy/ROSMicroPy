from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Float32(Message):
    _TYPE_NAME = 'Float32'
    _TYPE_DEF = _TYPE_DEFS['Float32']
    _fields_and_field_types = {'data': 'float32'}

    def __init__(self, data=None):
        self['data'] = 0.0 if data is None else data

dataMap = Float32.get_data_map()
