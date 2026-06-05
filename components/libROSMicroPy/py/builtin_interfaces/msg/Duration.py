from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Duration(Message):
    _TYPE_NAME = 'Duration'
    _TYPE_DEF = _TYPE_DEFS['Duration']
    _fields_and_field_types = {'sec': 'int32', 'nanosec': 'uint32'}

    def __init__(self, sec=None, nanosec=None):
        self['sec'] = 0 if sec is None else sec
        self['nanosec'] = 0 if nanosec is None else nanosec

dataMap = Duration.get_data_map()
