from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Vector3Stamped(Message):
    _TYPE_NAME = 'Vector3Stamped'
    _TYPE_DEF = _TYPE_DEFS['Vector3Stamped']
    _fields_and_field_types = {'header': 'Header', 'vector': 'Vector3'}

    def __init__(self, header=None, vector=None):
        self['header'] = {} if header is None else header
        self['vector'] = {} if vector is None else vector

dataMap = Vector3Stamped.get_data_map()
