from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class PointField(Message):
    _TYPE_NAME = 'PointField'
    _TYPE_DEF = _TYPE_DEFS['PointField']
    _fields_and_field_types = {'name': 'string', 'offset': 'uint32', 'datatype': 'uint8', 'count': 'uint32'}
    INT8 = 1
    UINT8 = 2
    INT16 = 3
    UINT16 = 4
    INT32 = 5
    UINT32 = 6
    FLOAT32 = 7
    FLOAT64 = 8

    def __init__(self, name=None, offset=None, datatype=None, count=None):
        self['name'] = '' if name is None else name
        self['offset'] = 0 if offset is None else offset
        self['datatype'] = 0 if datatype is None else datatype
        self['count'] = 0 if count is None else count

dataMap = PointField.get_data_map()
