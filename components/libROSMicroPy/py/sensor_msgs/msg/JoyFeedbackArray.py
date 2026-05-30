from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class JoyFeedbackArray(Message):
    _TYPE_NAME = 'JoyFeedbackArray'
    _TYPE_DEF = _TYPE_DEFS['JoyFeedbackArray']
    _fields_and_field_types = {'array': 'JoyFeedback'}

    def __init__(self, array=None):
        self['array'] = [] if array is None else array

dataMap = JoyFeedbackArray.get_data_map()
