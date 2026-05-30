from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class InertiaStamped(Message):
    _TYPE_NAME = 'InertiaStamped'
    _TYPE_DEF = _TYPE_DEFS['InertiaStamped']
    _fields_and_field_types = {'header': 'Header', 'inertia': 'Inertia'}

    def __init__(self, header=None, inertia=None):
        self['header'] = {} if header is None else header
        self['inertia'] = {} if inertia is None else inertia

dataMap = InertiaStamped.get_data_map()
