from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Inertia(Message):
    _TYPE_NAME = 'Inertia'
    _TYPE_DEF = _TYPE_DEFS['Inertia']
    _fields_and_field_types = {'m': 'float64', 'com': 'Vector3', 'ixx': 'float64', 'ixy': 'float64', 'ixz': 'float64', 'iyy': 'float64', 'iyz': 'float64', 'izz': 'float64'}

    def __init__(self, m=None, com=None, ixx=None, ixy=None, ixz=None, iyy=None, iyz=None, izz=None):
        self['m'] = 0.0 if m is None else m
        self['com'] = {} if com is None else com
        self['ixx'] = 0.0 if ixx is None else ixx
        self['ixy'] = 0.0 if ixy is None else ixy
        self['ixz'] = 0.0 if ixz is None else ixz
        self['iyy'] = 0.0 if iyy is None else iyy
        self['iyz'] = 0.0 if iyz is None else iyz
        self['izz'] = 0.0 if izz is None else izz

dataMap = Inertia.get_data_map()
