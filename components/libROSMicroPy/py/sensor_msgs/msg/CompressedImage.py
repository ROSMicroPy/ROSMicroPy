from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class CompressedImage(Message):
    _TYPE_NAME = 'CompressedImage'
    _TYPE_DEF = _TYPE_DEFS['CompressedImage']
    _fields_and_field_types = {'header': 'Header', 'format': 'string', 'data': 'uint8'}

    def __init__(self, header=None, format=None, data=None):
        self['header'] = {} if header is None else header
        self['format'] = '' if format is None else format
        self['data'] = [] if data is None else data

dataMap = CompressedImage.get_data_map()
