from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class Image(Message):
    _TYPE_NAME = 'Image'
    _TYPE_DEF = _TYPE_DEFS['Image']
    _fields_and_field_types = {'header': 'Header', 'height': 'uint32', 'width': 'uint32', 'encoding': 'string', 'is_bigendian': 'uint8', 'step': 'uint32', 'data': 'uint8'}

    def __init__(self, header=None, height=None, width=None, encoding=None, is_bigendian=None, step=None, data=None):
        self['header'] = {} if header is None else header
        self['height'] = 0 if height is None else height
        self['width'] = 0 if width is None else width
        self['encoding'] = '' if encoding is None else encoding
        self['is_bigendian'] = 0 if is_bigendian is None else is_bigendian
        self['step'] = 0 if step is None else step
        self['data'] = [] if data is None else data

dataMap = Image.get_data_map()
