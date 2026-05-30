from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class TwistStamped(Message):
    _TYPE_NAME = 'TwistStamped'
    _TYPE_DEF = _TYPE_DEFS['TwistStamped']
    _fields_and_field_types = {'header': 'Header', 'twist': 'Twist'}

    def __init__(self, header=None, twist=None):
        self['header'] = {} if header is None else header
        self['twist'] = {} if twist is None else twist

dataMap = TwistStamped.get_data_map()
