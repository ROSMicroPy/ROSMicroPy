from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Log(Message):
    _TYPE_NAME = 'Log'
    _TYPE_DEF = _TYPE_DEFS['Log']
    _fields_and_field_types = {'stamp': 'Time', 'level': 'uint8', 'name': 'string', 'msg': 'string', 'file': 'string', 'function': 'string', 'line': 'uint32'}
    DEBUG = 10
    INFO = 20
    WARN = 30
    ERROR = 40
    FATAL = 50

    def __init__(self, stamp=None, level=None, name=None, msg=None, file=None, function=None, line=None):
        self['stamp'] = {} if stamp is None else stamp
        self['level'] = 0 if level is None else level
        self['name'] = '' if name is None else name
        self['msg'] = '' if msg is None else msg
        self['file'] = '' if file is None else file
        self['function'] = '' if function is None else function
        self['line'] = 0 if line is None else line

dataMap = Log.get_data_map()
