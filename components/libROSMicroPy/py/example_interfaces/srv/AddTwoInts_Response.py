from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class AddTwoInts_Response(Message):
    _TYPE_NAME = 'AddTwoInts_Response'
    _TYPE_DEF = _TYPE_DEFS['AddTwoInts_Response']
    _fields_and_field_types = {'sum': 'int64'}

    def __init__(self, sum=None):
        self['sum'] = 0 if sum is None else sum

dataMap = AddTwoInts_Response.get_data_map()
