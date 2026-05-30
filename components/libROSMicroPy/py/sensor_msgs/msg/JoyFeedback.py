from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class JoyFeedback(Message):
    _TYPE_NAME = 'JoyFeedback'
    _TYPE_DEF = _TYPE_DEFS['JoyFeedback']
    _fields_and_field_types = {'type': 'uint8', 'id': 'uint8', 'intensity': 'float32'}
    TYPE_LED = 0
    TYPE_RUMBLE = 1
    TYPE_BUZZER = 2

    def __init__(self, type=None, id=None, intensity=None):
        self['type'] = 0 if type is None else type
        self['id'] = 0 if id is None else id
        self['intensity'] = 0.0 if intensity is None else intensity

dataMap = JoyFeedback.get_data_map()
