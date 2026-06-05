def make_component(spec):
    name, typ, children, is_array, is_sequence, cap = spec
    item = {'name': name, 'type': typ}
    if children:
        item['components'] = [make_component(child) for child in children]
    if is_array:
        item['isArray'] = True
    if is_sequence:
        item['isSequence'] = True
    if cap:
        item['capicity'] = cap
    return item

def make_data_map(type_def):
    name, namespace, fields = type_def
    return {'message_name': name, 'message_namespace': namespace, 'components': [make_component(field) for field in fields]}

class Message:
    _TYPE_NAME = ''
    _TYPE_DEF = None
    _fields_and_field_types = {}

    def __getitem__(self, name):
        try:
            return getattr(self, name)
        except AttributeError:
            raise KeyError(name)

    def __setitem__(self, name, value):
        setattr(self, name, value)

    def __contains__(self, name):
        return name in self.__dict__

    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def items(self):
        return self.__dict__.items()

    def keys(self):
        return self.__dict__.keys()

    def values(self):
        return self.__dict__.values()

    def get(self, name, default=None):
        return self.__dict__.get(name, default)

    @classmethod
    def get_fields_and_field_types(cls):
        return dict(cls._fields_and_field_types)

    @classmethod
    def get_data_map(cls):
        return make_data_map(cls._TYPE_DEF)

    @property
    def dataMap(self):
        return self.get_data_map()
