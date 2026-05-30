from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class TwistWithCovarianceStamped(Message):
    _TYPE_NAME = 'TwistWithCovarianceStamped'
    _TYPE_DEF = _TYPE_DEFS['TwistWithCovarianceStamped']
    _fields_and_field_types = {'header': 'Header', 'twist': 'TwistWithCovariance'}

    def __init__(self, header=None, twist=None):
        self['header'] = {} if header is None else header
        self['twist'] = {} if twist is None else twist

dataMap = TwistWithCovarianceStamped.get_data_map()
