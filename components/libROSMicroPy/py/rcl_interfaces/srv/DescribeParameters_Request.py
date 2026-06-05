from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class DescribeParameters_Request(Message):
    _TYPE_NAME = 'DescribeParameters_Request'
    _TYPE_DEF = _TYPE_DEFS['DescribeParameters_Request']
    _fields_and_field_types = {'names': 'string'}

    def __init__(self, names=None):
        self['names'] = [] if names is None else names

dataMap = DescribeParameters_Request.get_data_map()
