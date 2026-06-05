from rostype.Vector3 import Vector3

class Attachment():
    
    dataMap = {
        "message_name": "Attachment",
        "message_namespace": "rosmicropy::msg",
        "components": [
            {
                "name": "attachment",
                "type": "float64"
            }
        ]
    }
    
    def __init__(self, data):
        self.data = data
        pass

    
