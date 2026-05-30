from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GetPlan_Response(Message):
    _TYPE_NAME = 'GetPlan_Response'
    _TYPE_DEF = _TYPE_DEFS['GetPlan_Response']
    _fields_and_field_types = {'plan': 'Path'}

    def __init__(self, plan=None):
        self['plan'] = {} if plan is None else plan

dataMap = GetPlan_Response.get_data_map()
