from .Empty_Request import Empty_Request
from .Empty_Response import Empty_Response

class Empty:
    Request = Empty_Request
    Response = Empty_Response

__all__ = ["Empty"]
