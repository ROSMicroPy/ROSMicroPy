from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class MarkerArray(Message):
    _TYPE_NAME = 'MarkerArray'
    _TYPE_DEF = _TYPE_DEFS['MarkerArray']
    _fields_and_field_types = {'markers': 'Marker'}

    def __init__(self, markers=None):
        self['markers'] = [] if markers is None else markers

dataMap = MarkerArray.get_data_map()
