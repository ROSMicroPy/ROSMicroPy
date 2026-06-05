from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class ListParametersResult(Message):
    _TYPE_NAME = 'ListParametersResult'
    _TYPE_DEF = _TYPE_DEFS['ListParametersResult']
    _fields_and_field_types = {'names': 'string', 'prefixes': 'string'}

    def __init__(self, names=None, prefixes=None):
        self['names'] = [] if names is None else names
        self['prefixes'] = [] if prefixes is None else prefixes

dataMap = ListParametersResult.get_data_map()
