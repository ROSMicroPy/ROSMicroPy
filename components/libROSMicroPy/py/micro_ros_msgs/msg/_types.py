_TYPE_DEFS = {
    'Entity': ('Entity', 'micro_ros_msgs::msg', (('entity_type', 'byte', (), False, False, 0),)),
    'Graph': ('Graph', 'micro_ros_msgs::msg', (('nodes', 'Node', (('entities', 'Entity', (('entity_type', 'byte', (), False, False, 0),), False, True, 0),), False, True, 0),)),
    'Node': ('Node', 'micro_ros_msgs::msg', (('entities', 'Entity', (('entity_type', 'byte', (), False, False, 0),), False, True, 0),)),
}
