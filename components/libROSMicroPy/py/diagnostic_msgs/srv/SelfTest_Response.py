from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class SelfTest_Response(Message):
    _TYPE_NAME = 'SelfTest_Response'
    _TYPE_DEF = _TYPE_DEFS['SelfTest_Response']
    _fields_and_field_types = {'id': 'string', 'passed': 'byte', 'status': 'DiagnosticStatus'}

    def __init__(self, id=None, passed=None, status=None):
        self['id'] = '' if id is None else id
        self['passed'] = 0 if passed is None else passed
        self['status'] = [] if status is None else status

dataMap = SelfTest_Response.get_data_map()
