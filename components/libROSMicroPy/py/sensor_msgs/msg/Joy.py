from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Joy(Message):
    _TYPE_NAME = 'Joy'
    _TYPE_DEF = _TYPE_DEFS['Joy']
    _fields_and_field_types = {'header': 'Header', 'axes': 'float32', 'buttons': 'int32'}

    def __init__(self, header=None, axes=None, buttons=None):
        self['header'] = {} if header is None else header
        self['axes'] = [] if axes is None else axes
        self['buttons'] = [] if buttons is None else buttons

dataMap = Joy.get_data_map()
