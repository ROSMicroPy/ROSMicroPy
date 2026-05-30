from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class WrenchStamped(Message):
    _TYPE_NAME = 'WrenchStamped'
    _TYPE_DEF = _TYPE_DEFS['WrenchStamped']
    _fields_and_field_types = {'header': 'Header', 'wrench': 'Wrench'}

    def __init__(self, header=None, wrench=None):
        self['header'] = {} if header is None else header
        self['wrench'] = {} if wrench is None else wrench

dataMap = WrenchStamped.get_data_map()
