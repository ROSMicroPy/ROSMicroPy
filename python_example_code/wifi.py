import esp
import webrepl
import network
from ROSMicroPy import setNodeName, setAgentIP, setAgentPort

sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect('rosnet', 'MicroROSNet')
    while not sta_if.isconnected():
     pass

print('network config:', sta_if.ifconfig())


#webrepl.start()
#esp.osdebug(None)

import sys, select
print("Press Enter to boot to REPL")
i, o, e = select.select( [sys.stdin], [], [], 10 )
if (not i):
    #setNamespace("")
    setAgentIP("192.168.8.100")
    setAgentPort("8888")
 #   import RosBot_Teleop
