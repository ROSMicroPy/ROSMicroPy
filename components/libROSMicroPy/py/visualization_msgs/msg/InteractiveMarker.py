from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class InteractiveMarker(Message):
    _TYPE_NAME = 'InteractiveMarker'
    _TYPE_DEF = _TYPE_DEFS['InteractiveMarker']
    _fields_and_field_types = {'header': 'Header', 'pose': 'Pose', 'name': 'string', 'description': 'string', 'scale': 'float32', 'menu_entries': 'MenuEntry', 'controls': 'InteractiveMarkerControl'}

    def __init__(self, header=None, pose=None, name=None, description=None, scale=None, menu_entries=None, controls=None):
        self['header'] = {} if header is None else header
        self['pose'] = {} if pose is None else pose
        self['name'] = '' if name is None else name
        self['description'] = '' if description is None else description
        self['scale'] = 0.0 if scale is None else scale
        self['menu_entries'] = [] if menu_entries is None else menu_entries
        self['controls'] = [] if controls is None else controls

dataMap = InteractiveMarker.get_data_map()
