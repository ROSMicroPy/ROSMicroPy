from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class DiagnosticStatus(Message):
    _TYPE_NAME = 'DiagnosticStatus'
    _TYPE_DEF = _TYPE_DEFS['DiagnosticStatus']
    _fields_and_field_types = {'level': 'byte', 'name': 'string', 'message': 'string', 'hardware_id': 'string', 'values': 'KeyValue'}
    OK = 0
    WARN = 1
    ERROR = 2
    STALE = 3

    def __init__(self, level=None, name=None, message=None, hardware_id=None, values=None):
        self['level'] = 0 if level is None else level
        self['name'] = '' if name is None else name
        self['message'] = '' if message is None else message
        self['hardware_id'] = '' if hardware_id is None else hardware_id
        self['values'] = [] if values is None else values

dataMap = DiagnosticStatus.get_data_map()
