from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class NavSatFix(Message):
    _TYPE_NAME = 'NavSatFix'
    _TYPE_DEF = _TYPE_DEFS['NavSatFix']
    _fields_and_field_types = {'header': 'Header', 'status': 'NavSatStatus', 'latitude': 'float64', 'longitude': 'float64', 'altitude': 'float64', 'position_covariance': 'float64', 'position_covariance_type': 'uint8'}
    COVARIANCE_TYPE_UNKNOWN = 0
    COVARIANCE_TYPE_APPROXIMATED = 1
    COVARIANCE_TYPE_DIAGONAL_KNOWN = 2
    COVARIANCE_TYPE_KNOWN = 3

    def __init__(self, header=None, status=None, latitude=None, longitude=None, altitude=None, position_covariance=None, position_covariance_type=None):
        self['header'] = {} if header is None else header
        self['status'] = {} if status is None else status
        self['latitude'] = 0.0 if latitude is None else latitude
        self['longitude'] = 0.0 if longitude is None else longitude
        self['altitude'] = 0.0 if altitude is None else altitude
        self['position_covariance'] = [] if position_covariance is None else position_covariance
        self['position_covariance_type'] = 0 if position_covariance_type is None else position_covariance_type

dataMap = NavSatFix.get_data_map()
