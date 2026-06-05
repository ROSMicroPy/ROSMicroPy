from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class StatisticDataPoint(Message):
    _TYPE_NAME = 'StatisticDataPoint'
    _TYPE_DEF = _TYPE_DEFS['StatisticDataPoint']
    _fields_and_field_types = {'data_type': 'uint8', 'data': 'float64'}

    def __init__(self, data_type=None, data=None):
        self['data_type'] = 0 if data_type is None else data_type
        self['data'] = 0.0 if data is None else data

dataMap = StatisticDataPoint.get_data_map()
