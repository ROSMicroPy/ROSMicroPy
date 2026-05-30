from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class MeshFile(Message):
    _TYPE_NAME = 'MeshFile'
    _TYPE_DEF = _TYPE_DEFS['MeshFile']
    _fields_and_field_types = {'filename': 'string', 'data': 'uint8'}

    def __init__(self, filename=None, data=None):
        self['filename'] = '' if filename is None else filename
        self['data'] = [] if data is None else data

dataMap = MeshFile.get_data_map()
