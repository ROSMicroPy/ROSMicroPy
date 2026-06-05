from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class ServiceEventInfo(Message):
    _TYPE_NAME = 'ServiceEventInfo'
    _TYPE_DEF = _TYPE_DEFS['ServiceEventInfo']
    _fields_and_field_types = {'event_type': 'uint8', 'stamp': 'Time', 'client_gid': 'char', 'sequence_number': 'int64'}
    REQUEST_SENT = 0
    REQUEST_RECEIVED = 1
    RESPONSE_SENT = 2
    RESPONSE_RECEIVED = 3

    def __init__(self, event_type=None, stamp=None, client_gid=None, sequence_number=None):
        self['event_type'] = 0 if event_type is None else event_type
        self['stamp'] = {} if stamp is None else stamp
        self['client_gid'] = [] if client_gid is None else client_gid
        self['sequence_number'] = 0 if sequence_number is None else sequence_number

dataMap = ServiceEventInfo.get_data_map()
