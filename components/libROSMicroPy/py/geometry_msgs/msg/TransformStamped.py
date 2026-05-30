from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class TransformStamped(Message):
    _TYPE_NAME = 'TransformStamped'
    _TYPE_DEF = _TYPE_DEFS['TransformStamped']
    _fields_and_field_types = {'header': 'Header', 'child_frame_id': 'string', 'transform': 'Transform'}

    def __init__(self, header=None, child_frame_id=None, transform=None):
        self['header'] = {} if header is None else header
        self['child_frame_id'] = '' if child_frame_id is None else child_frame_id
        self['transform'] = {} if transform is None else transform

dataMap = TransformStamped.get_data_map()
