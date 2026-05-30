from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class ImageMarker(Message):
    _TYPE_NAME = 'ImageMarker'
    _TYPE_DEF = _TYPE_DEFS['ImageMarker']
    _fields_and_field_types = {'header': 'Header', 'ns': 'string', 'id': 'int32', 'type': 'int32', 'action': 'int32', 'position': 'Point', 'scale': 'float32', 'outline_color': 'ColorRGBA', 'filled': 'uint8', 'fill_color': 'ColorRGBA', 'lifetime': 'Duration', 'points': 'Point', 'outline_colors': 'ColorRGBA'}
    CIRCLE = 0
    LINE_STRIP = 1
    LINE_LIST = 2
    POLYGON = 3
    POINTS = 4
    ADD = 0
    REMOVE = 1

    def __init__(self, header=None, ns=None, id=None, type=None, action=None, position=None, scale=None, outline_color=None, filled=None, fill_color=None, lifetime=None, points=None, outline_colors=None):
        self['header'] = {} if header is None else header
        self['ns'] = '' if ns is None else ns
        self['id'] = 0 if id is None else id
        self['type'] = 0 if type is None else type
        self['action'] = 0 if action is None else action
        self['position'] = {} if position is None else position
        self['scale'] = 0.0 if scale is None else scale
        self['outline_color'] = {} if outline_color is None else outline_color
        self['filled'] = 0 if filled is None else filled
        self['fill_color'] = {} if fill_color is None else fill_color
        self['lifetime'] = {} if lifetime is None else lifetime
        self['points'] = [] if points is None else points
        self['outline_colors'] = [] if outline_colors is None else outline_colors

dataMap = ImageMarker.get_data_map()
