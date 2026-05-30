from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class InteractiveMarkerFeedback(Message):
    _TYPE_NAME = 'InteractiveMarkerFeedback'
    _TYPE_DEF = _TYPE_DEFS['InteractiveMarkerFeedback']
    _fields_and_field_types = {'header': 'Header', 'client_id': 'string', 'marker_name': 'string', 'control_name': 'string', 'event_type': 'uint8', 'pose': 'Pose', 'menu_entry_id': 'uint32', 'mouse_point': 'Point', 'mouse_point_valid': 'bool'}
    KEEP_ALIVE = 0
    POSE_UPDATE = 1
    MENU_SELECT = 2
    BUTTON_CLICK = 3
    MOUSE_DOWN = 4
    MOUSE_UP = 5

    def __init__(self, header=None, client_id=None, marker_name=None, control_name=None, event_type=None, pose=None, menu_entry_id=None, mouse_point=None, mouse_point_valid=None):
        self['header'] = {} if header is None else header
        self['client_id'] = '' if client_id is None else client_id
        self['marker_name'] = '' if marker_name is None else marker_name
        self['control_name'] = '' if control_name is None else control_name
        self['event_type'] = 0 if event_type is None else event_type
        self['pose'] = {} if pose is None else pose
        self['menu_entry_id'] = 0 if menu_entry_id is None else menu_entry_id
        self['mouse_point'] = {} if mouse_point is None else mouse_point
        self['mouse_point_valid'] = False if mouse_point_valid is None else mouse_point_valid

dataMap = InteractiveMarkerFeedback.get_data_map()
