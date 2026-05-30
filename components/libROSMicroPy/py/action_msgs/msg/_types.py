_TYPE_DEFS = {
    'GoalInfo': ('GoalInfo', 'action_msgs::msg', (('goal_id', 'UUID', (), False, False, 0), ('stamp', 'Time', (), False, False, 0))),
    'GoalStatus': ('GoalStatus', 'action_msgs::msg', (('goal_info', 'GoalInfo', (('goal_id', 'UUID', (), False, False, 0), ('stamp', 'Time', (), False, False, 0)), False, False, 0), ('status', 'int8', (), False, False, 0))),
    'GoalStatusArray': ('GoalStatusArray', 'action_msgs::msg', (('status_list', 'GoalStatus', (('goal_info', 'GoalInfo', (('goal_id', 'UUID', (), False, False, 0), ('stamp', 'Time', (), False, False, 0)), False, False, 0), ('status', 'int8', (), False, False, 0)), False, True, 0),)),
}
