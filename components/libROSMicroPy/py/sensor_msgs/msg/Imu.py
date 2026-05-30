from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Imu(Message):
    _TYPE_NAME = 'Imu'
    _TYPE_DEF = _TYPE_DEFS['Imu']
    _fields_and_field_types = {'header': 'Header', 'orientation': 'Quaternion', 'orientation_covariance': 'float64', 'angular_velocity': 'Vector3', 'angular_velocity_covariance': 'float64', 'linear_acceleration': 'Vector3', 'linear_acceleration_covariance': 'float64'}

    def __init__(self, header=None, orientation=None, orientation_covariance=None, angular_velocity=None, angular_velocity_covariance=None, linear_acceleration=None, linear_acceleration_covariance=None):
        self['header'] = {} if header is None else header
        self['orientation'] = {} if orientation is None else orientation
        self['orientation_covariance'] = [] if orientation_covariance is None else orientation_covariance
        self['angular_velocity'] = {} if angular_velocity is None else angular_velocity
        self['angular_velocity_covariance'] = [] if angular_velocity_covariance is None else angular_velocity_covariance
        self['linear_acceleration'] = {} if linear_acceleration is None else linear_acceleration
        self['linear_acceleration_covariance'] = [] if linear_acceleration_covariance is None else linear_acceleration_covariance

dataMap = Imu.get_data_map()
