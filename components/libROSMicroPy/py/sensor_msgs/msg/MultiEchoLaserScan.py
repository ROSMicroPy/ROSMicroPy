from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class MultiEchoLaserScan(Message):
    _TYPE_NAME = 'MultiEchoLaserScan'
    _TYPE_DEF = _TYPE_DEFS['MultiEchoLaserScan']
    _fields_and_field_types = {'header': 'Header', 'angle_min': 'float32', 'angle_max': 'float32', 'angle_increment': 'float32', 'time_increment': 'float32', 'scan_time': 'float32', 'range_min': 'float32', 'range_max': 'float32', 'ranges': 'LaserEcho', 'intensities': 'LaserEcho'}

    def __init__(self, header=None, angle_min=None, angle_max=None, angle_increment=None, time_increment=None, scan_time=None, range_min=None, range_max=None, ranges=None, intensities=None):
        self['header'] = {} if header is None else header
        self['angle_min'] = 0.0 if angle_min is None else angle_min
        self['angle_max'] = 0.0 if angle_max is None else angle_max
        self['angle_increment'] = 0.0 if angle_increment is None else angle_increment
        self['time_increment'] = 0.0 if time_increment is None else time_increment
        self['scan_time'] = 0.0 if scan_time is None else scan_time
        self['range_min'] = 0.0 if range_min is None else range_min
        self['range_max'] = 0.0 if range_max is None else range_max
        self['ranges'] = [] if ranges is None else ranges
        self['intensities'] = [] if intensities is None else intensities

dataMap = MultiEchoLaserScan.get_data_map()
