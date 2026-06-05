from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class IndividualTypeDescription(Message):
    _TYPE_NAME = 'IndividualTypeDescription'
    _TYPE_DEF = _TYPE_DEFS['IndividualTypeDescription']
    _fields_and_field_types = {'fields': 'Field'}

    def __init__(self, fields=None):
        self['fields'] = [] if fields is None else fields

dataMap = IndividualTypeDescription.get_data_map()
