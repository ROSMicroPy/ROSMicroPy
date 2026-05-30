from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class AccelWithCovariance(Message):
    _TYPE_NAME = 'AccelWithCovariance'
    _TYPE_DEF = _TYPE_DEFS['AccelWithCovariance']
    _fields_and_field_types = {'accel': 'Accel', 'covariance': 'float64'}

    def __init__(self, accel=None, covariance=None):
        self['accel'] = {} if accel is None else accel
        self['covariance'] = [] if covariance is None else covariance

dataMap = AccelWithCovariance.get_data_map()
