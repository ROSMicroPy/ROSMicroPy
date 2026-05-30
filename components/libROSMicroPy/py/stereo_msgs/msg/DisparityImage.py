from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class DisparityImage(Message):
    _TYPE_NAME = 'DisparityImage'
    _TYPE_DEF = _TYPE_DEFS['DisparityImage']
    _fields_and_field_types = {'header': 'Header', 'image': 'Image', 'f': 'float32', 't': 'float32', 'valid_window': 'RegionOfInterest', 'min_disparity': 'float32', 'max_disparity': 'float32', 'delta_d': 'float32'}

    def __init__(self, header=None, image=None, f=None, t=None, valid_window=None, min_disparity=None, max_disparity=None, delta_d=None):
        self['header'] = {} if header is None else header
        self['image'] = {} if image is None else image
        self['f'] = 0.0 if f is None else f
        self['t'] = 0.0 if t is None else t
        self['valid_window'] = {} if valid_window is None else valid_window
        self['min_disparity'] = 0.0 if min_disparity is None else min_disparity
        self['max_disparity'] = 0.0 if max_disparity is None else max_disparity
        self['delta_d'] = 0.0 if delta_d is None else delta_d

dataMap = DisparityImage.get_data_map()
