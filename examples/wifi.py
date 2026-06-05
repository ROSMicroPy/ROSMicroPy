import network

wlan = network.WLAN(network.STA_IF) # create station interface

wlan.active(True)       # activate the interface
wlan.scan()             # scan for access points

wlan.config('mac')      # get the interface's MAC address
wlan.ipconfig('addr4')  # get the interface's IPv4 addresses

sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect('rosnet', 'MicroROSNet')
    while not sta_if.isconnected():
        pass

print('network config:', sta_if.ifconfig())