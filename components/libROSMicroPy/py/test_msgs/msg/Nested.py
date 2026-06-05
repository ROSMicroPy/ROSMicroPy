from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Nested(Message):
    _TYPE_NAME = 'Nested'
    _TYPE_DEF = _TYPE_DEFS['Nested']
    _fields_and_field_types = {'basic_types_value': 'BasicTypes'}

    def __init__(self, basic_types_value=None):
        self['basic_types_value'] = {} if basic_types_value is None else basic_types_value

dataMap = Nested.get_data_map()
