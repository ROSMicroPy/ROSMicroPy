from rostype.Vector3 import Vector3

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

    def __init__(self, data):
        self.data = data
        pass

    def Linear():
        return Vector3(data.linear)
    
    def Angular():
        return Vector3(data.angular)
    