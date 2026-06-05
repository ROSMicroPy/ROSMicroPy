from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class LoadNode_Response(Message):
    _TYPE_NAME = 'LoadNode_Response'
    _TYPE_DEF = _TYPE_DEFS['LoadNode_Response']
    _fields_and_field_types = {'success': 'bool', 'error_message': 'string', 'full_node_name': 'string', 'unique_id': 'uint64'}

    def __init__(self, success=None, error_message=None, full_node_name=None, unique_id=None):
        self['success'] = False if success is None else success
        self['error_message'] = '' if error_message is None else error_message
        self['full_node_name'] = '' if full_node_name is None else full_node_name
        self['unique_id'] = 0 if unique_id is None else unique_id

dataMap = LoadNode_Response.get_data_map()
