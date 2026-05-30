from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Transform(Message):
    _TYPE_NAME = 'Transform'
    _TYPE_DEF = _TYPE_DEFS['Transform']
    _fields_and_field_types = {'translation': 'Vector3', 'rotation': 'Quaternion'}

    def __init__(self, translation=None, rotation=None):
        self['translation'] = {} if translation is None else translation
        self['rotation'] = {} if rotation is None else rotation

dataMap = Transform.get_data_map()
