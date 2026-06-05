from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Action(Message):
    _TYPE_NAME = 'Action'
    _TYPE_DEF = _TYPE_DEFS['Action']
    _fields_and_field_types = {'name': 'string', 'send_goal': 'Service', 'get_result': 'Service', 'cancel_goal': 'Service', 'feedback': 'Topic', 'status': 'Topic'}

    def __init__(self, name=None, send_goal=None, get_result=None, cancel_goal=None, feedback=None, status=None):
        self['name'] = '' if name is None else name
        self['send_goal'] = {} if send_goal is None else send_goal
        self['get_result'] = {} if get_result is None else get_result
        self['cancel_goal'] = {} if cancel_goal is None else cancel_goal
        self['feedback'] = {} if feedback is None else feedback
        self['status'] = {} if status is None else status

dataMap = Action.get_data_map()
