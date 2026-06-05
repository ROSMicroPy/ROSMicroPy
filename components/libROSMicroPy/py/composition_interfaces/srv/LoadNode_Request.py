from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class LoadNode_Request(Message):
    _TYPE_NAME = 'LoadNode_Request'
    _TYPE_DEF = _TYPE_DEFS['LoadNode_Request']
    _fields_and_field_types = {'package_name': 'string', 'plugin_name': 'string', 'node_name': 'string', 'node_namespace': 'string', 'log_level': 'uint8', 'remap_rules': 'string', 'parameters': 'Parameter', 'extra_arguments': 'Parameter'}

    def __init__(self, package_name=None, plugin_name=None, node_name=None, node_namespace=None, log_level=None, remap_rules=None, parameters=None, extra_arguments=None):
        self['package_name'] = '' if package_name is None else package_name
        self['plugin_name'] = '' if plugin_name is None else plugin_name
        self['node_name'] = '' if node_name is None else node_name
        self['node_namespace'] = '' if node_namespace is None else node_namespace
        self['log_level'] = 0 if log_level is None else log_level
        self['remap_rules'] = [] if remap_rules is None else remap_rules
        self['parameters'] = [] if parameters is None else parameters
        self['extra_arguments'] = [] if extra_arguments is None else extra_arguments

dataMap = LoadNode_Request.get_data_map()
