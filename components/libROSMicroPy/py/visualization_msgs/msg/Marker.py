from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Marker(Message):
    _TYPE_NAME = 'Marker'
    _TYPE_DEF = _TYPE_DEFS['Marker']
    _fields_and_field_types = {'header': 'Header', 'ns': 'string', 'id': 'int32', 'type': 'int32', 'action': 'int32', 'pose': 'Pose', 'scale': 'Vector3', 'color': 'ColorRGBA', 'lifetime': 'Duration', 'frame_locked': 'bool', 'points': 'Point', 'colors': 'ColorRGBA', 'texture_resource': 'string', 'texture': 'CompressedImage', 'uv_coordinates': 'UVCoordinate', 'text': 'string', 'mesh_resource': 'string', 'mesh_file': 'MeshFile', 'mesh_use_embedded_materials': 'bool'}
    ARROW = 0
    CUBE = 1
    SPHERE = 2
    CYLINDER = 3
    LINE_STRIP = 4
    LINE_LIST = 5
    CUBE_LIST = 6
    SPHERE_LIST = 7
    POINTS = 8
    TEXT_VIEW_FACING = 9
    MESH_RESOURCE = 10
    TRIANGLE_LIST = 11
    ARROW_STRIP = 12
    ADD = 0
    MODIFY = 0
    DELETE = 2
    DELETEALL = 3

    def __init__(self, header=None, ns=None, id=None, type=None, action=None, pose=None, scale=None, color=None, lifetime=None, frame_locked=None, points=None, colors=None, texture_resource=None, texture=None, uv_coordinates=None, text=None, mesh_resource=None, mesh_file=None, mesh_use_embedded_materials=None):
        self['header'] = {} if header is None else header
        self['ns'] = '' if ns is None else ns
        self['id'] = 0 if id is None else id
        self['type'] = 0 if type is None else type
        self['action'] = 0 if action is None else action
        self['pose'] = {} if pose is None else pose
        self['scale'] = {} if scale is None else scale
        self['color'] = {} if color is None else color
        self['lifetime'] = {} if lifetime is None else lifetime
        self['frame_locked'] = False if frame_locked is None else frame_locked
        self['points'] = [] if points is None else points
        self['colors'] = [] if colors is None else colors
        self['texture_resource'] = '' if texture_resource is None else texture_resource
        self['texture'] = {} if texture is None else texture
        self['uv_coordinates'] = [] if uv_coordinates is None else uv_coordinates
        self['text'] = '' if text is None else text
        self['mesh_resource'] = '' if mesh_resource is None else mesh_resource
        self['mesh_file'] = {} if mesh_file is None else mesh_file
        self['mesh_use_embedded_materials'] = False if mesh_use_embedded_materials is None else mesh_use_embedded_materials

dataMap = Marker.get_data_map()
