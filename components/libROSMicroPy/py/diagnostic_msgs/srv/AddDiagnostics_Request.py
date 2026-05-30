from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class AddDiagnostics_Request(Message):
    _TYPE_NAME = 'AddDiagnostics_Request'
    _TYPE_DEF = _TYPE_DEFS['AddDiagnostics_Request']
    _fields_and_field_types = {'load_namespace': 'string'}

    def __init__(self, load_namespace=None):
        self['load_namespace'] = '' if load_namespace is None else load_namespace

dataMap = AddDiagnostics_Request.get_data_map()
