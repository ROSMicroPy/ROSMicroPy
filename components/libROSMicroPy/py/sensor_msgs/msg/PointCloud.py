from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class PointCloud(Message):
    _TYPE_NAME = 'PointCloud'
    _TYPE_DEF = _TYPE_DEFS['PointCloud']
    _fields_and_field_types = {'header': 'Header', 'points': 'Point32', 'channels': 'ChannelFloat32'}

    def __init__(self, header=None, points=None, channels=None):
        self['header'] = {} if header is None else header
        self['points'] = [] if points is None else points
        self['channels'] = [] if channels is None else channels

dataMap = PointCloud.get_data_map()
