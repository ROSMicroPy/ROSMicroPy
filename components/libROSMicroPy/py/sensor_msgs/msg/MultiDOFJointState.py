from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class MultiDOFJointState(Message):
    _TYPE_NAME = 'MultiDOFJointState'
    _TYPE_DEF = _TYPE_DEFS['MultiDOFJointState']
    _fields_and_field_types = {'header': 'Header', 'joint_names': 'string', 'transforms': 'Transform', 'twist': 'Twist', 'wrench': 'Wrench'}

    def __init__(self, header=None, joint_names=None, transforms=None, twist=None, wrench=None):
        self['header'] = {} if header is None else header
        self['joint_names'] = [] if joint_names is None else joint_names
        self['transforms'] = [] if transforms is None else transforms
        self['twist'] = [] if twist is None else twist
        self['wrench'] = [] if wrench is None else wrench

dataMap = MultiDOFJointState.get_data_map()
