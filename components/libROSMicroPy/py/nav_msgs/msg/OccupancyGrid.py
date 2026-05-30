from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class OccupancyGrid(Message):
    _TYPE_NAME = 'OccupancyGrid'
    _TYPE_DEF = _TYPE_DEFS['OccupancyGrid']
    _fields_and_field_types = {'header': 'Header', 'info': 'MapMetaData', 'data': 'int8'}

    def __init__(self, header=None, info=None, data=None):
        self['header'] = {} if header is None else header
        self['info'] = {} if info is None else info
        self['data'] = [] if data is None else data

dataMap = OccupancyGrid.get_data_map()
