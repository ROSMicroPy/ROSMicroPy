from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class PointStamped(Message):
    _TYPE_NAME = 'PointStamped'
    _TYPE_DEF = _TYPE_DEFS['PointStamped']
    _fields_and_field_types = {'header': 'Header', 'point': 'Point'}

    def __init__(self, header=None, point=None):
        self['header'] = {} if header is None else header
        self['point'] = {} if point is None else point

dataMap = PointStamped.get_data_map()
