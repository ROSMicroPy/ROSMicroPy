from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Range(Message):
    _TYPE_NAME = 'Range'
    _TYPE_DEF = _TYPE_DEFS['Range']
    _fields_and_field_types = {'header': 'Header', 'radiation_type': 'uint8', 'field_of_view': 'float32', 'min_range': 'float32', 'max_range': 'float32', 'range': 'float32', 'variance': 'float32'}
    ULTRASOUND = 0
    INFRARED = 1

    def __init__(self, header=None, radiation_type=None, field_of_view=None, min_range=None, max_range=None, range=None, variance=None):
        self['header'] = {} if header is None else header
        self['radiation_type'] = 0 if radiation_type is None else radiation_type
        self['field_of_view'] = 0.0 if field_of_view is None else field_of_view
        self['min_range'] = 0.0 if min_range is None else min_range
        self['max_range'] = 0.0 if max_range is None else max_range
        self['range'] = 0.0 if range is None else range
        self['variance'] = 0.0 if variance is None else variance

dataMap = Range.get_data_map()
