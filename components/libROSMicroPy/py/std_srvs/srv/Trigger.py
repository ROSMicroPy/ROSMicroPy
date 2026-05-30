from .Trigger_Request import Trigger_Request
from .Trigger_Response import Trigger_Response

class Trigger:
    Request = Trigger_Request
    Response = Trigger_Response

__all__ = ["Trigger"]
