from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class NavSatStatus(Message):
    _TYPE_NAME = 'NavSatStatus'
    _TYPE_DEF = _TYPE_DEFS['NavSatStatus']
    _fields_and_field_types = {'status': 'int8', 'service': 'uint16'}
    STATUS_UNKNOWN = -2
    STATUS_NO_FIX = -1
    STATUS_FIX = 0
    STATUS_SBAS_FIX = 1
    STATUS_GBAS_FIX = 2
    SERVICE_UNKNOWN = 0
    SERVICE_GPS = 1
    SERVICE_GLONASS = 2
    SERVICE_COMPASS = 4
    SERVICE_GALILEO = 8

    def __init__(self, status=None, service=None):
        self['status'] = 0 if status is None else status
        self['service'] = 0 if service is None else service

dataMap = NavSatStatus.get_data_map()
