from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Float64(Message):
    _TYPE_NAME = 'Float64'
    _TYPE_DEF = _TYPE_DEFS['Float64']
    _fields_and_field_types = {'data': 'float64'}

    def __init__(self, data=None):
        self['data'] = 0.0 if data is None else data

dataMap = Float64.get_data_map()
