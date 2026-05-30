from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class TwistWithCovariance(Message):
    _TYPE_NAME = 'TwistWithCovariance'
    _TYPE_DEF = _TYPE_DEFS['TwistWithCovariance']
    _fields_and_field_types = {'twist': 'Twist', 'covariance': 'float64'}

    def __init__(self, twist=None, covariance=None):
        self['twist'] = {} if twist is None else twist
        self['covariance'] = [] if covariance is None else covariance

dataMap = TwistWithCovariance.get_data_map()
