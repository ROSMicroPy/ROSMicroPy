from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GetTypeDescription_Response(Message):
    _TYPE_NAME = 'GetTypeDescription_Response'
    _TYPE_DEF = _TYPE_DEFS['GetTypeDescription_Response']
    _fields_and_field_types = {'successful': 'bool', 'failure_reason': 'string', 'type_description': 'TypeDescription', 'type_sources': 'TypeSource', 'extra_information': 'KeyValue'}

    def __init__(self, successful=None, failure_reason=None, type_description=None, type_sources=None, extra_information=None):
        self['successful'] = False if successful is None else successful
        self['failure_reason'] = '' if failure_reason is None else failure_reason
        self['type_description'] = {} if type_description is None else type_description
        self['type_sources'] = [] if type_sources is None else type_sources
        self['extra_information'] = [] if extra_information is None else extra_information

dataMap = GetTypeDescription_Response.get_data_map()
