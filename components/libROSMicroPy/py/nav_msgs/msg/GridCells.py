from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class GridCells(Message):
    _TYPE_NAME = 'GridCells'
    _TYPE_DEF = _TYPE_DEFS['GridCells']
    _fields_and_field_types = {'header': 'Header', 'cell_width': 'float32', 'cell_height': 'float32', 'cells': 'Point'}

    def __init__(self, header=None, cell_width=None, cell_height=None, cells=None):
        self['header'] = {} if header is None else header
        self['cell_width'] = 0.0 if cell_width is None else cell_width
        self['cell_height'] = 0.0 if cell_height is None else cell_height
        self['cells'] = [] if cells is None else cells

dataMap = GridCells.get_data_map()
