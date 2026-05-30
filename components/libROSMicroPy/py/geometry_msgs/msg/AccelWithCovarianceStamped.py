from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class AccelWithCovarianceStamped(Message):
    _TYPE_NAME = 'AccelWithCovarianceStamped'
    _TYPE_DEF = _TYPE_DEFS['AccelWithCovarianceStamped']
    _fields_and_field_types = {'header': 'Header', 'accel': 'AccelWithCovariance'}

    def __init__(self, header=None, accel=None):
        self['header'] = {} if header is None else header
        self['accel'] = {} if accel is None else accel

dataMap = AccelWithCovarianceStamped.get_data_map()
