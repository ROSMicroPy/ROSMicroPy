from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class BoundedPlainSequences(Message):
    _TYPE_NAME = 'BoundedPlainSequences'
    _TYPE_DEF = _TYPE_DEFS['BoundedPlainSequences']
    _fields_and_field_types = {'alignment_check': 'int32'}

    def __init__(self, alignment_check=None):
        self['alignment_check'] = 0 if alignment_check is None else alignment_check

dataMap = BoundedPlainSequences.get_data_map()
