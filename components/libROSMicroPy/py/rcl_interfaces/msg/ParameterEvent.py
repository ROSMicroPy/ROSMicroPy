from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class ParameterEvent(Message):
    _TYPE_NAME = 'ParameterEvent'
    _TYPE_DEF = _TYPE_DEFS['ParameterEvent']
    _fields_and_field_types = {'stamp': 'Time', 'node': 'string', 'new_parameters': 'Parameter', 'changed_parameters': 'Parameter', 'deleted_parameters': 'Parameter'}

    def __init__(self, stamp=None, node=None, new_parameters=None, changed_parameters=None, deleted_parameters=None):
        self['stamp'] = {} if stamp is None else stamp
        self['node'] = '' if node is None else node
        self['new_parameters'] = [] if new_parameters is None else new_parameters
        self['changed_parameters'] = [] if changed_parameters is None else changed_parameters
        self['deleted_parameters'] = [] if deleted_parameters is None else deleted_parameters

dataMap = ParameterEvent.get_data_map()
