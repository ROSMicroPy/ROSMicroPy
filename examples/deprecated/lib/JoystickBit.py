from machine import Pin, ADC
import machine

from time import sleep
import _thread

class joystickbit():
    
    def __init__(self) -> None:
        
        self.xaxis = ADC(Pin(32))
        self.xaxis.atten(ADC.ATTN_11DB)

        self.yaxis = ADC(Pin(34))  #25 33
        self.yaxis.atten(ADC.ATTN_11DB)
        self.yaxis.width(ADC.WIDTH_12BIT)
        
        self.bUp =    machine.Pin(18, machine.Pin.IN, machine.Pin.PULL_UP)
        self.bDown =  machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)
        self.bRight = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
        self.bLeft  = machine.Pin(23, machine.Pin.IN, machine.Pin.PULL_UP)
                       
        self.xval:int = 0
        self.yval:int = 0
        self.bUpVal:int = 1
        self.bDownVal:int = 1
        self.bRightVal:int = 1
        self.bLeftVal:int = 1
        
        self._onButtonUp: callable[[int], None] = None
        self._onButtonDown: callable[[int], None] = None
        self._onButtonLeft: callable[[int], None] = None
        self._onButtonRight: callable[[int], None] = None
        self._onY: callable[[int], None] = None
        self._onX: callable[[int], None] = None
        
        self.xCenter:int = 0
        self.yCenter:int = 0
        
        self.lock = _thread.allocate_lock()        
        
        self.calibrateJoystick()
        _thread.start_new_thread(self.loop, ())


    def onButton_Up(self, func: callable[[int], None]):
        with self.lock:
            self._onButtonUp = func
        
    def onButton_Down(self, func: callable[[int], None]):
        with self.lock:
            self._onButtonDown = func
        
    def onButton_Left(self, func: callable[[int], None]):
        with self.lock:
            self._onButtonLeft = func
        
    def onButton_Right(self, func: callable[[int], None]):
        with self.lock:
            self._onButtonRight = func
    
    def onJoystick_Y(self, func: callable[[int], None]):
        with self.lock:
            self._onY = func
        
    def onJoystick_X(self, func: callable[[int], None]):
        with self.lock:
            self._onX = func
        
    def loop(self):
        #print("Enter Loop")

        _self = self
        
        while True:
            sleep(0.2)
            
            #
            # Grab new values
            #
            with _self.lock:
                xval:int = _self.xaxis.read_u16() >> 8
                yval:int = _self.yaxis.read_u16() >> 8
                xval = xval-self.xCenter
                yval = yval-self.yCenter
                
                bUpVal:int = _self.bUp.value()
                bDownVal:int = _self.bDown.value()
                bRightVal:int = _self.bRight.value()
                bLeftVal:int = _self.bLeft.value()
            
            #
            # Detect change and call back
            #
            with _self.lock:
                xdiff:int = _self.xval - xval
                trigger = abs(xdiff)
#                print(f"X self:{_self.xval} val:{xval} T:{trigger} diff:{xdiff}")

                if ( trigger > 10):
#                    print("T")
                    if(_self._onX):
                        _self._onX(xval)
                    
            with _self.lock:
                ydiff:int = _self.yval - yval
                trigger = abs(ydiff)
#                print(f"Y self:{_self.yval} val:{yval} T:{trigger} diff:{ydiff}")

                if (trigger > 10):
                    if(_self._onY):
                        _self._onY(yval)
            
            with _self.lock:
                if (_self.bUpVal != bUpVal):
                    if (_self._onButtonUp):
                        _self._onButtonUp(bUpVal)

            with _self.lock:
                if (_self.bDownVal != bDownVal):
                    if (_self._onButtonDown):
                        _self._onButtonDown(bDownVal)
                
            with _self.lock:
                if (_self.bRightVal != bRightVal):
                    if (_self._onButtonRight):
                        _self._onButtonRight(bRightVal)
                
            with _self.lock:
                if (_self.bLeftVal != bLeftVal):
                    if (_self._onButtonLeft):
                        _self._onButtonLeft(bLeftVal)
            
            #
            # Store last read values in self.
            #
            with _self.lock:
                _self.xval = xval
                _self.yval = yval
                
                _self.bUpVal = bUpVal
                _self.bDownVal = bDownVal
                _self.bRightVal = bRightVal
                _self.bLeftVal = bLeftVal

    def calibrateJoystick(self):
        print ("Calibrating Joystick")
        xCenter:int = 0
        yCenter:int = 0
        for x in range(200):
            xval:int = self.xaxis.read_u16() >> 8
            yval:int = self.yaxis.read_u16() >> 8
            xCenter = xCenter + xval
            yCenter = yCenter + yval
        
        self.xCenter = xCenter/200
        self.yCenter = yCenter/200
        
        print (f"Calibration Complete X:{self.xCenter} Y:{self.yCenter}")
        
        
    def printValues(self):
        print(f"x axis {self.xval}")
        print(f"y axis {self.yval}")
        
        print(f"Up {self.bUpVal}")
        print(f"Down {self.bDownVal}")
        print(f"left {self.bRightVal}")
        print(f"right {self.bLeftVal}")
            

    #def Vibration_Motor(time: number) -> None: 
    #    pins.digitalWritePin(DigitalPin.P16, 0)
    #    basic.pause(time)
    #    pins.digitalWritePin(DigitalPin.P16, 1)
    
