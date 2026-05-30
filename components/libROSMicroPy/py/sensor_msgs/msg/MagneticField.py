from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class MagneticField(Message):
    _TYPE_NAME = 'MagneticField'
    _TYPE_DEF = _TYPE_DEFS['MagneticField']
    _fields_and_field_types = {'header': 'Header', 'magnetic_field': 'Vector3', 'magnetic_field_covariance': 'float64'}

    def __init__(self, header=None, magnetic_field=None, magnetic_field_covariance=None):
        self['header'] = {} if header is None else header
        self['magnetic_field'] = {} if magnetic_field is None else magnetic_field
        self['magnetic_field_covariance'] = [] if magnetic_field_covariance is None else magnetic_field_covariance

dataMap = MagneticField.get_data_map()
