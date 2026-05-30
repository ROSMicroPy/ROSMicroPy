_TYPE_DEFS = {
    'AddDiagnostics_Request': ('AddDiagnostics_Request', 'diagnostic_msgs::srv', (('load_namespace', 'string', (), False, False, 0),)),
    'AddDiagnostics_Response': ('AddDiagnostics_Response', 'diagnostic_msgs::srv', (('success', 'bool', (), False, False, 0), ('message', 'string', (), False, False, 0))),
    'SelfTest_Request': ('SelfTest_Request', 'diagnostic_msgs::srv', ()),
    'SelfTest_Response': ('SelfTest_Response', 'diagnostic_msgs::srv', (('id', 'string', (), False, False, 0), ('passed', 'byte', (), False, False, 0), ('status', 'DiagnosticStatus', (('level', 'byte', (), False, False, 0), ('name', 'string', (), False, False, 0), ('message', 'string', (), False, False, 0), ('hardware_id', 'string', (), False, False, 0), ('values', 'KeyValue', (('key', 'string', (), False, False, 0), ('value', 'string', (), False, False, 0)), False, True, 0)), False, True, 0))),
}
