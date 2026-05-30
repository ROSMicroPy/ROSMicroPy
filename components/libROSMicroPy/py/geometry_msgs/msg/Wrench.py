from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Wrench(Message):
    _TYPE_NAME = 'Wrench'
    _TYPE_DEF = _TYPE_DEFS['Wrench']
    _fields_and_field_types = {'force': 'Vector3', 'torque': 'Vector3'}

    def __init__(self, force=None, torque=None):
        self['force'] = {} if force is None else force
        self['torque'] = {} if torque is None else torque

dataMap = Wrench.get_data_map()
