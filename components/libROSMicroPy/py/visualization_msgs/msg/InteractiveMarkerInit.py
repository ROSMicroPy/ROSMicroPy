from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class InteractiveMarkerInit(Message):
    _TYPE_NAME = 'InteractiveMarkerInit'
    _TYPE_DEF = _TYPE_DEFS['InteractiveMarkerInit']
    _fields_and_field_types = {'server_id': 'string', 'seq_num': 'uint64', 'markers': 'InteractiveMarker'}

    def __init__(self, server_id=None, seq_num=None, markers=None):
        self['server_id'] = '' if server_id is None else server_id
        self['seq_num'] = 0 if seq_num is None else seq_num
        self['markers'] = [] if markers is None else markers

dataMap = InteractiveMarkerInit.get_data_map()
