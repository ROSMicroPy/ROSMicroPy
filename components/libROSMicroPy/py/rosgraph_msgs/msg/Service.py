from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Service(Message):
    _TYPE_NAME = 'Service'
    _TYPE_DEF = _TYPE_DEFS['Service']
    _fields_and_field_types = {'name': 'string', 'request_type': 'InterfaceType', 'request_qos': 'QoSProfile', 'response_type': 'InterfaceType', 'response_qos': 'QoSProfile'}

    def __init__(self, name=None, request_type=None, request_qos=None, response_type=None, response_qos=None):
        self['name'] = '' if name is None else name
        self['request_type'] = {} if request_type is None else request_type
        self['request_qos'] = {} if request_qos is None else request_qos
        self['response_type'] = {} if response_type is None else response_type
        self['response_qos'] = {} if response_qos is None else response_qos

dataMap = Service.get_data_map()
