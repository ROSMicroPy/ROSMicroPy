from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class ListNodes_Response(Message):
    _TYPE_NAME = 'ListNodes_Response'
    _TYPE_DEF = _TYPE_DEFS['ListNodes_Response']
    _fields_and_field_types = {'full_node_names': 'string', 'unique_ids': 'uint64'}

    def __init__(self, full_node_names=None, unique_ids=None):
        self['full_node_names'] = [] if full_node_names is None else full_node_names
        self['unique_ids'] = [] if unique_ids is None else unique_ids

dataMap = ListNodes_Response.get_data_map()
