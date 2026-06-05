from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class TypeSource(Message):
    _TYPE_NAME = 'TypeSource'
    _TYPE_DEF = _TYPE_DEFS['TypeSource']
    _fields_and_field_types = {'type_name': 'string', 'encoding': 'string', 'raw_file_contents': 'string'}

    def __init__(self, type_name=None, encoding=None, raw_file_contents=None):
        self['type_name'] = '' if type_name is None else type_name
        self['encoding'] = '' if encoding is None else encoding
        self['raw_file_contents'] = '' if raw_file_contents is None else raw_file_contents

dataMap = TypeSource.get_data_map()
