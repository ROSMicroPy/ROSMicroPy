from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class JointState(Message):
    _TYPE_NAME = 'JointState'
    _TYPE_DEF = _TYPE_DEFS['JointState']
    _fields_and_field_types = {'header': 'Header', 'name': 'string', 'position': 'float64', 'velocity': 'float64', 'effort': 'float64'}

    def __init__(self, header=None, name=None, position=None, velocity=None, effort=None):
        self['header'] = {} if header is None else header
        self['name'] = [] if name is None else name
        self['position'] = [] if position is None else position
        self['velocity'] = [] if velocity is None else velocity
        self['effort'] = [] if effort is None else effort

dataMap = JointState.get_data_map()
