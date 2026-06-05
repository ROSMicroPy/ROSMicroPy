from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class WStrings(Message):
    _TYPE_NAME = 'WStrings'
    _TYPE_DEF = _TYPE_DEFS['WStrings']
    _fields_and_field_types = {'wstring_value': 'string', 'wstring_value_default1': 'string', 'wstring_value_default2': 'string', 'wstring_value_default3': 'string', 'array_of_wstrings': 'string', 'unbounded_sequence_of_wstrings': 'string'}

    def __init__(self, wstring_value=None, wstring_value_default1=None, wstring_value_default2=None, wstring_value_default3=None, array_of_wstrings=None, unbounded_sequence_of_wstrings=None):
        self['wstring_value'] = '' if wstring_value is None else wstring_value
        self['wstring_value_default1'] = '' if wstring_value_default1 is None else wstring_value_default1
        self['wstring_value_default2'] = '' if wstring_value_default2 is None else wstring_value_default2
        self['wstring_value_default3'] = '' if wstring_value_default3 is None else wstring_value_default3
        self['array_of_wstrings'] = [] if array_of_wstrings is None else array_of_wstrings
        self['unbounded_sequence_of_wstrings'] = [] if unbounded_sequence_of_wstrings is None else unbounded_sequence_of_wstrings

dataMap = WStrings.get_data_map()
