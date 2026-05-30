from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class CameraInfo(Message):
    _TYPE_NAME = 'CameraInfo'
    _TYPE_DEF = _TYPE_DEFS['CameraInfo']
    _fields_and_field_types = {'header': 'Header', 'height': 'uint32', 'width': 'uint32', 'distortion_model': 'string', 'd': 'float64', 'k': 'float64', 'r': 'float64', 'p': 'float64', 'binning_x': 'uint32', 'binning_y': 'uint32', 'roi': 'RegionOfInterest'}

    def __init__(self, header=None, height=None, width=None, distortion_model=None, d=None, k=None, r=None, p=None, binning_x=None, binning_y=None, roi=None):
        self['header'] = {} if header is None else header
        self['height'] = 0 if height is None else height
        self['width'] = 0 if width is None else width
        self['distortion_model'] = '' if distortion_model is None else distortion_model
        self['d'] = [] if d is None else d
        self['k'] = [] if k is None else k
        self['r'] = [] if r is None else r
        self['p'] = [] if p is None else p
        self['binning_x'] = 0 if binning_x is None else binning_x
        self['binning_y'] = 0 if binning_y is None else binning_y
        self['roi'] = {} if roi is None else roi

dataMap = CameraInfo.get_data_map()
