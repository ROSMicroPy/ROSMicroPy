from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class DescribeParameters_Response(Message):
    _TYPE_NAME = 'DescribeParameters_Response'
    _TYPE_DEF = _TYPE_DEFS['DescribeParameters_Response']
    _fields_and_field_types = {'descriptors': 'ParameterDescriptor'}

    def __init__(self, descriptors=None):
        self['descriptors'] = [] if descriptors is None else descriptors

dataMap = DescribeParameters_Response.get_data_map()
