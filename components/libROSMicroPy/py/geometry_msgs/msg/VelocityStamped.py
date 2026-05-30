from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class VelocityStamped(Message):
    _TYPE_NAME = 'VelocityStamped'
    _TYPE_DEF = _TYPE_DEFS['VelocityStamped']
    _fields_and_field_types = {'header': 'Header', 'body_frame_id': 'string', 'reference_frame_id': 'string', 'velocity': 'Twist'}

    def __init__(self, header=None, body_frame_id=None, reference_frame_id=None, velocity=None):
        self['header'] = {} if header is None else header
        self['body_frame_id'] = '' if body_frame_id is None else body_frame_id
        self['reference_frame_id'] = '' if reference_frame_id is None else reference_frame_id
        self['velocity'] = {} if velocity is None else velocity

dataMap = VelocityStamped.get_data_map()
