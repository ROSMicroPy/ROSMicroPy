from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class MenuEntry(Message):
    _TYPE_NAME = 'MenuEntry'
    _TYPE_DEF = _TYPE_DEFS['MenuEntry']
    _fields_and_field_types = {'id': 'uint32', 'parent_id': 'uint32', 'title': 'string', 'command': 'string', 'command_type': 'uint8'}
    FEEDBACK = 0
    ROSRUN = 1
    ROSLAUNCH = 2

    def __init__(self, id=None, parent_id=None, title=None, command=None, command_type=None):
        self['id'] = 0 if id is None else id
        self['parent_id'] = 0 if parent_id is None else parent_id
        self['title'] = '' if title is None else title
        self['command'] = '' if command is None else command
        self['command_type'] = 0 if command_type is None else command_type

dataMap = MenuEntry.get_data_map()
