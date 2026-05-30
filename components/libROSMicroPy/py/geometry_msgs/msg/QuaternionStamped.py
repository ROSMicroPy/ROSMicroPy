from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class QuaternionStamped(Message):
    _TYPE_NAME = 'QuaternionStamped'
    _TYPE_DEF = _TYPE_DEFS['QuaternionStamped']
    _fields_and_field_types = {'header': 'Header', 'quaternion': 'Quaternion'}

    def __init__(self, header=None, quaternion=None):
        self['header'] = {} if header is None else header
        self['quaternion'] = {} if quaternion is None else quaternion

dataMap = QuaternionStamped.get_data_map()
