from rosmicropy_interfaces import Message
from ._types import _TYPE_DEFS

class MultiNested(Message):
    _TYPE_NAME = 'MultiNested'
    _TYPE_DEF = _TYPE_DEFS['MultiNested']
    _fields_and_field_types = {'array_of_arrays': 'Arrays', 'array_of_bounded_sequences': 'BoundedSequences', 'array_of_unbounded_sequences': 'UnboundedSequences', 'unbounded_sequence_of_arrays': 'Arrays', 'unbounded_sequence_of_bounded_sequences': 'BoundedSequences', 'unbounded_sequence_of_unbounded_sequences': 'UnboundedSequences'}

    def __init__(self, array_of_arrays=None, array_of_bounded_sequences=None, array_of_unbounded_sequences=None, unbounded_sequence_of_arrays=None, unbounded_sequence_of_bounded_sequences=None, unbounded_sequence_of_unbounded_sequences=None):
        self['array_of_arrays'] = [] if array_of_arrays is None else array_of_arrays
        self['array_of_bounded_sequences'] = [] if array_of_bounded_sequences is None else array_of_bounded_sequences
        self['array_of_unbounded_sequences'] = [] if array_of_unbounded_sequences is None else array_of_unbounded_sequences
        self['unbounded_sequence_of_arrays'] = [] if unbounded_sequence_of_arrays is None else unbounded_sequence_of_arrays
        self['unbounded_sequence_of_bounded_sequences'] = [] if unbounded_sequence_of_bounded_sequences is None else unbounded_sequence_of_bounded_sequences
        self['unbounded_sequence_of_unbounded_sequences'] = [] if unbounded_sequence_of_unbounded_sequences is None else unbounded_sequence_of_unbounded_sequences

dataMap = MultiNested.get_data_map()
