from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class MapMetaData(Message):
    _TYPE_NAME = 'MapMetaData'
    _TYPE_DEF = _TYPE_DEFS['MapMetaData']
    _fields_and_field_types = {'map_load_time': 'Time', 'resolution': 'float32', 'width': 'uint32', 'height': 'uint32', 'origin': 'Pose'}

    def __init__(self, map_load_time=None, resolution=None, width=None, height=None, origin=None):
        self['map_load_time'] = {} if map_load_time is None else map_load_time
        self['resolution'] = 0.0 if resolution is None else resolution
        self['width'] = 0 if width is None else width
        self['height'] = 0 if height is None else height
        self['origin'] = {} if origin is None else origin

dataMap = MapMetaData.get_data_map()
