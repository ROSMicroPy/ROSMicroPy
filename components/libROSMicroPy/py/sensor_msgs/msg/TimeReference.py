from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class TimeReference(Message):
    _TYPE_NAME = 'TimeReference'
    _TYPE_DEF = _TYPE_DEFS['TimeReference']
    _fields_and_field_types = {'header': 'Header', 'time_ref': 'Time', 'source': 'string'}

    def __init__(self, header=None, time_ref=None, source=None):
        self['header'] = {} if header is None else header
        self['time_ref'] = {} if time_ref is None else time_ref
        self['source'] = '' if source is None else source

dataMap = TimeReference.get_data_map()
