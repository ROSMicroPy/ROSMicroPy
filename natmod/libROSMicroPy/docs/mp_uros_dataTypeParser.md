/**
 * The MicroROS <-> Micropython Type Support function will support  
 * 
 **/


https://github.com/gentijo/ROSMicroPy-TypeGen

The Schema is as follows:

A List of Dict entries where the Dictionary contains a Name / Type and a list of sub types. This list will also be flattened out. 
I.e. 
+ A Geometry _Twist message consists of two Vector3, 
    + Vector3 messages consists of 3 doubles, a primitive type. 

```
class Twist():
    
    dataMap = {
    "name": "optional",
    "type": "Twist",
    "components": [
        {
            "name": "linear",
            "type": "Vector3",
            "components": [
                {
                    "name": "x",
                    "type": "Double"
                },
                {
                    "name": "y",
                    "type": "Double"
                },
                {
                    "name": "z",
                    "type": "Double"
                }
            ]
        },
        {
            "name": "angular",
            "type": "Vector3",
            "components": [
                {
                    "name": "x",
                    "type": "Double"
                },
                {
                    "name": "y",
                    "type": "Double"
                },
                {
                    "name": "z",
                    "type": "Double"
                }
            ]
        }
    ]
}
```