# ROS Type Support in Micropython 

### ROS Types in Micropython are defined at runtime using a 2 step process.
### * .msg files -> converted to -> Python object
### * Python object -> a ROSMicroPy type support instruction list

[MicroROS RTIDL](https://github.com/gentijo/MicroROS-RTIDL) is a project that will automate the conversion from .msg files to Python object.
This code can run on the device or a computer then upload the Python objects to the device. 

Python object can be hand crafted also. 


An example of this schema is here [Geometry:Twist](../../python_example_code/rostype/Twist.py)



    class Twist():
        
        dataMap = {
            "message_name": "Twist",
            "message_namespace": "geometry_msgs::msg",
            "components": [
                {
                    "name": "linear",
                    "type": "Vector3",
                    "components": [
                        {
                            "name": "x",
                            "type": "float64"
                        },
                        {
                            "name": "y",
                            "type": "float64"
                        },
                        {
                            "name": "z",
                            "type": "float64"
                        }
                    ]
                },
                {
                    "name": "angular",
                    "type": "Vector3",
                    "components": [
                        {
                            "name": "x",
                            "type": "float64"
                        },
                        {
                            "name": "y",
                            "type": "float64"
                        },
                        {
                            "name": "z",
                            "type": "float64"
                        }
                    ]
                }
            ]
        }


    
### The python object can be registered with the system, then the typeSupport object can be used to 
        
    typeTwist = registerDataType(Twist.dataMap)

    #
    # dumpDataType is used to output the instruction list for the Python Object
    # This is used for Diagnostic purposes and can be deleted.
    #
    dumpDataType(typeTwist)
    
    print("Registering Event Publishers\r\n")
    pubCmdVel = registerROSPublisher("turtle1/cmd_vel", typeTwist)

