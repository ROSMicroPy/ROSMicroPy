from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Node(Message):
    _TYPE_NAME = 'Node'
    _TYPE_DEF = _TYPE_DEFS['Node']
    _fields_and_field_types = {'name': 'string', 'parameters': 'ParameterDescriptor', 'parameter_values': 'ParameterValue', 'publishers': 'Topic', 'subscriptions': 'Topic', 'service_clients': 'Service', 'service_servers': 'Service', 'action_clients': 'Action', 'action_servers': 'Action'}

    def __init__(self, name=None, parameters=None, parameter_values=None, publishers=None, subscriptions=None, service_clients=None, service_servers=None, action_clients=None, action_servers=None):
        self['name'] = '' if name is None else name
        self['parameters'] = [] if parameters is None else parameters
        self['parameter_values'] = [] if parameter_values is None else parameter_values
        self['publishers'] = [] if publishers is None else publishers
        self['subscriptions'] = [] if subscriptions is None else subscriptions
        self['service_clients'] = [] if service_clients is None else service_clients
        self['service_servers'] = [] if service_servers is None else service_servers
        self['action_clients'] = [] if action_clients is None else action_clients
        self['action_servers'] = [] if action_servers is None else action_servers

dataMap = Node.get_data_map()
