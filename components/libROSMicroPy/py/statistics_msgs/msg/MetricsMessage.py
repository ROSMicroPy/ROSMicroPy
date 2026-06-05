from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class MetricsMessage(Message):
    _TYPE_NAME = 'MetricsMessage'
    _TYPE_DEF = _TYPE_DEFS['MetricsMessage']
    _fields_and_field_types = {'measurement_source_name': 'string', 'metrics_source': 'string', 'unit': 'string', 'window_start': 'Time', 'window_stop': 'Time', 'statistics': 'StatisticDataPoint'}

    def __init__(self, measurement_source_name=None, metrics_source=None, unit=None, window_start=None, window_stop=None, statistics=None):
        self['measurement_source_name'] = '' if measurement_source_name is None else measurement_source_name
        self['metrics_source'] = '' if metrics_source is None else metrics_source
        self['unit'] = '' if unit is None else unit
        self['window_start'] = {} if window_start is None else window_start
        self['window_stop'] = {} if window_stop is None else window_stop
        self['statistics'] = [] if statistics is None else statistics

dataMap = MetricsMessage.get_data_map()
