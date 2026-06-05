from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class TypeDescription(Message):
    _TYPE_NAME = 'TypeDescription'
    _TYPE_DEF = _TYPE_DEFS['TypeDescription']
    _fields_and_field_types = {'type_description': 'IndividualTypeDescription', 'referenced_type_descriptions': 'IndividualTypeDescription'}

    def __init__(self, type_description=None, referenced_type_descriptions=None):
        self['type_description'] = {} if type_description is None else type_description
        self['referenced_type_descriptions'] = [] if referenced_type_descriptions is None else referenced_type_descriptions

dataMap = TypeDescription.get_data_map()
