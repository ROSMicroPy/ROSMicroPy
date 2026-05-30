from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class RegionOfInterest(Message):
    _TYPE_NAME = 'RegionOfInterest'
    _TYPE_DEF = _TYPE_DEFS['RegionOfInterest']
    _fields_and_field_types = {'x_offset': 'uint32', 'y_offset': 'uint32', 'height': 'uint32', 'width': 'uint32', 'do_rectify': 'bool'}

    def __init__(self, x_offset=None, y_offset=None, height=None, width=None, do_rectify=None):
        self['x_offset'] = 0 if x_offset is None else x_offset
        self['y_offset'] = 0 if y_offset is None else y_offset
        self['height'] = 0 if height is None else height
        self['width'] = 0 if width is None else width
        self['do_rectify'] = False if do_rectify is None else do_rectify

dataMap = RegionOfInterest.get_data_map()
