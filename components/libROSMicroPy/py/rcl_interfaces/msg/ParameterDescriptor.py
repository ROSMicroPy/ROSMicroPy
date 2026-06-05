from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class ParameterDescriptor(Message):
    _TYPE_NAME = 'ParameterDescriptor'
    _TYPE_DEF = _TYPE_DEFS['ParameterDescriptor']
    _fields_and_field_types = {'name': 'string', 'type': 'uint8', 'description': 'string', 'additional_constraints': 'string', 'read_only': 'bool', 'dynamic_typing': 'bool'}

    def __init__(self, name=None, type=None, description=None, additional_constraints=None, read_only=None, dynamic_typing=None):
        self['name'] = '' if name is None else name
        self['type'] = 0 if type is None else type
        self['description'] = '' if description is None else description
        self['additional_constraints'] = '' if additional_constraints is None else additional_constraints
        self['read_only'] = False if read_only is None else read_only
        self['dynamic_typing'] = False if dynamic_typing is None else dynamic_typing

dataMap = ParameterDescriptor.get_data_map()
