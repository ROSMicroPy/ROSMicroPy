from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Parameter(Message):
    _TYPE_NAME = 'Parameter'
    _TYPE_DEF = _TYPE_DEFS['Parameter']
    _fields_and_field_types = {'name': 'string', 'value': 'ParameterValue'}

    def __init__(self, name=None, value=None):
        self['name'] = '' if name is None else name
        self['value'] = {} if value is None else value

dataMap = Parameter.get_data_map()
