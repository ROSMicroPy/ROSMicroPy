from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GetInteractiveMarkers_Response(Message):
    _TYPE_NAME = 'GetInteractiveMarkers_Response'
    _TYPE_DEF = _TYPE_DEFS['GetInteractiveMarkers_Response']
    _fields_and_field_types = {'sequence_number': 'uint64', 'markers': 'InteractiveMarker'}

    def __init__(self, sequence_number=None, markers=None):
        self['sequence_number'] = 0 if sequence_number is None else sequence_number
        self['markers'] = [] if markers is None else markers

dataMap = GetInteractiveMarkers_Response.get_data_map()
