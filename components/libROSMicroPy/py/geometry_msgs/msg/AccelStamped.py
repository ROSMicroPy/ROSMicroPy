from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class AccelStamped(Message):
    _TYPE_NAME = 'AccelStamped'
    _TYPE_DEF = _TYPE_DEFS['AccelStamped']
    _fields_and_field_types = {'header': 'Header', 'accel': 'Accel'}

    def __init__(self, header=None, accel=None):
        self['header'] = {} if header is None else header
        self['accel'] = {} if accel is None else accel

dataMap = AccelStamped.get_data_map()
