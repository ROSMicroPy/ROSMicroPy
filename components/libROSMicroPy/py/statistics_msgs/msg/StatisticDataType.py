from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class StatisticDataType(Message):
    _TYPE_NAME = 'StatisticDataType'
    _TYPE_DEF = _TYPE_DEFS['StatisticDataType']
    _fields_and_field_types = {}
    STATISTICS_DATA_TYPE_UNINITIALIZED = 0
    STATISTICS_DATA_TYPE_AVERAGE = 1
    STATISTICS_DATA_TYPE_MINIMUM = 2
    STATISTICS_DATA_TYPE_MAXIMUM = 3
    STATISTICS_DATA_TYPE_STDDEV = 4
    STATISTICS_DATA_TYPE_SAMPLE_COUNT = 5

    def __init__(self):
        pass

dataMap = StatisticDataType.get_data_map()
