from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class SetParametersResult(Message):
    _TYPE_NAME = 'SetParametersResult'
    _TYPE_DEF = _TYPE_DEFS['SetParametersResult']
    _fields_and_field_types = {'successful': 'bool', 'reason': 'string'}

    def __init__(self, successful=None, reason=None):
        self['successful'] = False if successful is None else successful
        self['reason'] = '' if reason is None else reason

dataMap = SetParametersResult.get_data_map()
