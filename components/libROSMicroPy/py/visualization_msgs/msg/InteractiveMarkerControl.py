from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class InteractiveMarkerControl(Message):
    _TYPE_NAME = 'InteractiveMarkerControl'
    _TYPE_DEF = _TYPE_DEFS['InteractiveMarkerControl']
    _fields_and_field_types = {'name': 'string', 'orientation': 'Quaternion', 'orientation_mode': 'uint8', 'interaction_mode': 'uint8', 'always_visible': 'bool', 'markers': 'Marker', 'independent_marker_orientation': 'bool', 'description': 'string'}
    INHERIT = 0
    FIXED = 1
    VIEW_FACING = 2
    NONE = 0
    MENU = 1
    BUTTON = 2
    MOVE_AXIS = 3
    MOVE_PLANE = 4
    ROTATE_AXIS = 5
    MOVE_ROTATE = 6
    MOVE_3D = 7
    ROTATE_3D = 8
    MOVE_ROTATE_3D = 9

    def __init__(self, name=None, orientation=None, orientation_mode=None, interaction_mode=None, always_visible=None, markers=None, independent_marker_orientation=None, description=None):
        self['name'] = '' if name is None else name
        self['orientation'] = {} if orientation is None else orientation
        self['orientation_mode'] = 0 if orientation_mode is None else orientation_mode
        self['interaction_mode'] = 0 if interaction_mode is None else interaction_mode
        self['always_visible'] = False if always_visible is None else always_visible
        self['markers'] = [] if markers is None else markers
        self['independent_marker_orientation'] = False if independent_marker_orientation is None else independent_marker_orientation
        self['description'] = '' if description is None else description

dataMap = InteractiveMarkerControl.get_data_map()
