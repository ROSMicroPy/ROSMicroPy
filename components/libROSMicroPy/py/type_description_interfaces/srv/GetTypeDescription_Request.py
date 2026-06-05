from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GetTypeDescription_Request(Message):
    _TYPE_NAME = 'GetTypeDescription_Request'
    _TYPE_DEF = _TYPE_DEFS['GetTypeDescription_Request']
    _fields_and_field_types = {'type_name': 'string', 'type_hash': 'string', 'include_type_sources': 'bool'}

    def __init__(self, type_name=None, type_hash=None, include_type_sources=None):
        self['type_name'] = '' if type_name is None else type_name
        self['type_hash'] = '' if type_hash is None else type_hash
        self['include_type_sources'] = False if include_type_sources is None else include_type_sources

dataMap = GetTypeDescription_Request.get_data_map()
