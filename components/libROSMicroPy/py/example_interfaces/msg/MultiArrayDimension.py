from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class MultiArrayDimension(Message):
    _TYPE_NAME = 'MultiArrayDimension'
    _TYPE_DEF = _TYPE_DEFS['MultiArrayDimension']
    _fields_and_field_types = {'label': 'string', 'size': 'uint32', 'stride': 'uint32'}

    def __init__(self, label=None, size=None, stride=None):
        self['label'] = '' if label is None else label
        self['size'] = 0 if size is None else size
        self['stride'] = 0 if stride is None else stride

dataMap = MultiArrayDimension.get_data_map()
