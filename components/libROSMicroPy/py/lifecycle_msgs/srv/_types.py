_TYPE_DEFS = {
    'ChangeState_Request': ('ChangeState_Request', 'lifecycle_msgs::srv', (('transition', 'Transition', (('id', 'uint8', (), False, False, 0), ('label', 'string', (), False, False, 0)), False, False, 0),)),
    'ChangeState_Response': ('ChangeState_Response', 'lifecycle_msgs::srv', (('success', 'bool', (), False, False, 0),)),
    'GetAvailableStates_Request': ('GetAvailableStates_Request', 'lifecycle_msgs::srv', ()),
    'GetAvailableStates_Response': ('GetAvailableStates_Response', 'lifecycle_msgs::srv', (('available_states', 'State', (('id', 'uint8', (), False, False, 0), ('label', 'string', (), False, False, 0)), False, True, 0),)),
    'GetAvailableTransitions_Request': ('GetAvailableTransitions_Request', 'lifecycle_msgs::srv', ()),
    'GetAvailableTransitions_Response': ('GetAvailableTransitions_Response', 'lifecycle_msgs::srv', (('available_transitions', 'TransitionDescription', (('transition', 'Transition', (('id', 'uint8', (), False, False, 0), ('label', 'string', (), False, False, 0)), False, False, 0), ('start_state', 'State', (('id', 'uint8', (), False, False, 0), ('label', 'string', (), False, False, 0)), False, False, 0), ('goal_state', 'State', (('id', 'uint8', (), False, False, 0), ('label', 'string', (), False, False, 0)), False, False, 0)), False, True, 0),)),
    'GetState_Request': ('GetState_Request', 'lifecycle_msgs::srv', ()),
    'GetState_Response': ('GetState_Response', 'lifecycle_msgs::srv', (('current_state', 'State', (('id', 'uint8', (), False, False, 0), ('label', 'string', (), False, False, 0)), False, False, 0),)),
}
