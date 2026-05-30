from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class PointCloud2(Message):
    _TYPE_NAME = 'PointCloud2'
    _TYPE_DEF = _TYPE_DEFS['PointCloud2']
    _fields_and_field_types = {'header': 'Header', 'height': 'uint32', 'width': 'uint32', 'fields': 'PointField', 'is_bigendian': 'bool', 'point_step': 'uint32', 'row_step': 'uint32', 'data': 'uint8', 'is_dense': 'bool'}

    def __init__(self, header=None, height=None, width=None, fields=None, is_bigendian=None, point_step=None, row_step=None, data=None, is_dense=None):
        self['header'] = {} if header is None else header
        self['height'] = 0 if height is None else height
        self['width'] = 0 if width is None else width
        self['fields'] = [] if fields is None else fields
        self['is_bigendian'] = False if is_bigendian is None else is_bigendian
        self['point_step'] = 0 if point_step is None else point_step
        self['row_step'] = 0 if row_step is None else row_step
        self['data'] = [] if data is None else data
        self['is_dense'] = False if is_dense is None else is_dense

dataMap = PointCloud2.get_data_map()
