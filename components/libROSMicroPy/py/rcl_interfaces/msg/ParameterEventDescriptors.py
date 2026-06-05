from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class ParameterEventDescriptors(Message):
    _TYPE_NAME = 'ParameterEventDescriptors'
    _TYPE_DEF = _TYPE_DEFS['ParameterEventDescriptors']
    _fields_and_field_types = {'new_parameters': 'ParameterDescriptor', 'changed_parameters': 'ParameterDescriptor', 'deleted_parameters': 'ParameterDescriptor'}

    def __init__(self, new_parameters=None, changed_parameters=None, deleted_parameters=None):
        self['new_parameters'] = [] if new_parameters is None else new_parameters
        self['changed_parameters'] = [] if changed_parameters is None else changed_parameters
        self['deleted_parameters'] = [] if deleted_parameters is None else deleted_parameters

dataMap = ParameterEventDescriptors.get_data_map()
