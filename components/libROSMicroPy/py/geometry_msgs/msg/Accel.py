from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Accel(Message):
    _TYPE_NAME = 'Accel'
    _TYPE_DEF = _TYPE_DEFS['Accel']
    _fields_and_field_types = {'linear': 'Vector3', 'angular': 'Vector3'}

    def __init__(self, linear=None, angular=None):
        self['linear'] = {} if linear is None else linear
        self['angular'] = {} if angular is None else angular

dataMap = Accel.get_data_map()
