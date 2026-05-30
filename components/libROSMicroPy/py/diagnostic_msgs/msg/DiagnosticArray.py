from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class DiagnosticArray(Message):
    _TYPE_NAME = 'DiagnosticArray'
    _TYPE_DEF = _TYPE_DEFS['DiagnosticArray']
    _fields_and_field_types = {'header': 'Header', 'status': 'DiagnosticStatus'}

    def __init__(self, header=None, status=None):
        self['header'] = {} if header is None else header
        self['status'] = [] if status is None else status

dataMap = DiagnosticArray.get_data_map()
