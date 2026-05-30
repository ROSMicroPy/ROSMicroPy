# ROSMicroPy Type Support Integration

[See Python Example for a high level explanation of Type Support](../python-dev/type-support.md)

The Python Object is parsed with the [mp_uros_dataTypeParser](../../extra_packages/ROSMicroPy/mp_uros_type_support/mp_uros_dataTypeParser.c)

This will produce an Instruction list, 
    Registering Data Type

    Type name: Twist
    Message Namespace: [geometry_msgs::msg] Name: [Twist]
    Number of components 8
    Instruction List:
    Type: [Root]  Name: [Root] IsROSType: [1] isLastBlk: [172]  shallow count:[2]
    Type: [Vector3]  Name: [linear] IsROSType: [1] isLastBlk: [0]  shallow count:[3]
    Type: [float64]  Name: [x] IsROSType: [0] isLastBlk: [0]  shallow count:[0]
    Type: [float64]  Name: [y] IsROSType: [0] isLastBlk: [0]  shallow count:[0]
    Type: [float64]  Name: [z] IsROSType: [0] isLastBlk: [1]  shallow count:[0]
    Type: [Vector3]  Name: [angular] IsROSType: [1] isLastBlk: [0]  shallow count:[3]
    Type: [float64]  Name: [x] IsROSType: [0] isLastBlk: [0]  shallow count:[0]
    Type: [float64]  Name: [y] IsROSType: [0] isLastBlk: [0]  shallow count:[0]
    Type: [float64]  Name: [z] IsROSType: [0] isLastBlk: [1]  shallow count:[0]

By default there are slots to Support Type support, there is a special Macro [typeSupportEntry](../../extra_packages/ROSMicroPy/mp_uros_type_support/mp_uros_type_support.c#32) that provides code that will inject context letting the generic Type Support find the Instruction list. 

The slots are defined here [Type Support Slots](../../extra_packages/ROSMicroPy/mp_uros_type_support/mp_uros_type_support.c#79)

The function [void init_mpy_ROS_TypeSupport(void)](../../extra_packages/ROSMicroPy/mp_uros_type_support/mp_uros_type_support.c#29) takes advantage where the method can defined sub methods and code. It is important to recognize that the function will both create code *at compile time* then initialize the array at runtime, both are needed so that the function reference from the generated code can be referenced at runtime

The generated code provides the Slot number context used by the generic Serialize / Deserialize functions

[bool mpy_uros_typesupport_cdr_serialize(int slot, const void *untyped_ros_message, ucdrBuffer *cdr)](../../extra_packages/ROSMicroPy/mp_uros_type_support/mp_uros_type_support.c#151)

[bool mpy_uros_typesupport_cdr_deserialize(int slot, ucdrBuffer *cdr, void *untyped_ros_message)](../../extra_packages/ROSMicroPy/mp_uros_type_support/mp_uros_type_support.c#201)

