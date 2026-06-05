from machine import I2C

import array
import machine
import utime

#
#
#
class MaqueenDrive:

    Motor_Left:int = 0
    Motor_Right:int = 1
    Both_Motors:int = 2

    Motor_Forward:int = 1
    Motor_Reverse:int = 2

    LEFT_MOTOR_REGISTER:int = 0
    RIGHT_MOTOR_REGISTER:int  = 2

    RIGHT_DISTANCE_REGISTER:int = 4
    LEFT_DISTANCE_REGISTER:int = 4
    DISTANCE_REGISTER:int = 4
    
    Maqueen_I2C_DevAddr:int = 0x10
    
    #
    #
    #
    def __init__(self, i2c=None):
        self.i2c=i2c
            
    #
    #
    #
    def forward(self, speed:int):
        
        # a speed less than 40 is unstable
        if (speed < 40): speed=40
        
        buf = bytearray(4)
        buf[0] = MaqueenDrive.Motor_Forward
        buf[1] = speed
        buf[2] = MaqueenDrive.Motor_Forward
        buf[3] = speed
        self.i2c.writeto_mem(
          MaqueenDrive.Maqueen_I2C_DevAddr, 
          MaqueenDrive.LEFT_MOTOR_REGISTER,
          buf)

    #
    #
    #
    def backward(self, speed:int):
        #
        # a speed less than 40 is unstable
        if (speed < 40): speed=40
        
        buf = bytearray(4)
        buf[0] = MaqueenDrive.Motor_Reverse
        buf[1] = speed
        buf[2] = MaqueenDrive.Motor_Reverse
        buf[3] = speed       
        self.i2c.writeto_mem(
          MaqueenDrive.Maqueen_I2C_DevAddr, 
          MaqueenDrive.LEFT_MOTOR_REGISTER,
          buf)
    #
    #
    #
    def turnLeft(self, speed:int, radius:int):

        if (speed < 35): speed = 35

        buf = bytearray(4)
        buf[0] = MaqueenDrive.Motor_Forward
        buf[1] = speed
        buf[2] = MaqueenDrive.Motor_Reverse
        buf[3] = speed

        self.i2c.writeto_mem(
          MaqueenDrive.Maqueen_I2C_DevAddr, 
          MaqueenDrive.LEFT_MOTOR_REGISTER,
          buf)

    #
    #
    #
    def turnRight(self, speed:int, radius:int):

        if (speed < 35): speed = 35
        buf = bytearray(4)
        buf[0] = MaqueenDrive.Motor_Reverse
        buf[1] = speed
        buf[2] = MaqueenDrive.Motor_Forward
        buf[3] = speed
        self.i2c.writeto_mem(
          MaqueenDrive.Maqueen_I2C_DevAddr, 
          MaqueenDrive.LEFT_MOTOR_REGISTER,
          buf)

#
# 
#
    def stop(self):
        speed:int = 0;
        buf = bytearray(4)
        buf[0] = MaqueenDrive.Motor_Forward
        buf[1] = speed
        buf[2] = MaqueenDrive.Motor_Forward
        buf[3] = speed
        self.i2c.writeto_mem(
          MaqueenDrive.Maqueen_I2C_DevAddr, 
          MaqueenDrive.LEFT_MOTOR_REGISTER,
          buf)


    #
    #
    #
    def readDistance(self, MotorID:int) -> int:
      distance:int

      buf:bytes = self.i2c.readfrom_mem(
        MaqueenDrive.Maqueen_I2C_DevAddr, 
        MaqueenDrive.LEFT_MOTOR_REGISTER, 4)

      if (MotorID == MaqueenDrive.Motor_Left):
        distance = ((buf[0] << 8 | buf[1]) * 10) / 900

      else:
        distance = ((buf[2] << 8 | buf[3]) * 10) / 900
    
      return distance


    #
    #
    #
    def clearDistance(self, MotorID:int):
      if (MotorID == MaqueenDrive.Motor_Left):
        buf = bytearray(1)
        buf[0] = 0
        
        self.i2c.writeto_mem(
          MaqueenDrive.Maqueen_I2C_DevAddr, 
          MaqueenDrive.LEFT_DISTANCE_REGISTER,
          buf)
      
      elif (MotorID == MaqueenDrive.Motor_Right):
        buf = bytearray(1)
        buf[0] = 0
        
        self.i2c.writeto_mem(
          MaqueenDrive.Maqueen_I2C_DevAddr, 
          MaqueenDrive.RIGHT_DISTANCE_REGISTER,
          buf)
      
      else:
        buf = bytearray(3)
        buf[0] = 0
        buf[1] = 0
        buf[2] = 0
        self.i2c.writeto_mem(
          MaqueenDrive.Maqueen_I2C_DevAddr, 
          MaqueenDrive.LEFT_DISTANCE_REGISTER,
          buf)     
        

    #
    #
    #
    def readSpeed(self, MotorID:int) -> int:
      speed:int = 0

      buf:bytes = self.i2c.readfrom_mem(
        MaqueenDrive.Maqueen_I2C_DevAddr, 
        MaqueenDrive.LEFT_MOTOR_REGISTER, 4)


      if (MotorID == MaqueenDrive.Motor_Left):
        if ((round(buf[1]) < 20) and (round(buf[1]) != 0)):
          speed = round(buf[1]) + 255

      elif (motorID == MaqueenDrive.Motor_Right):
  
          if ((round(buf[3]) < 20) and (round(buf[3]) != 0)):
            speed = round(buf[3]) + 255

      else:
        speed = round(buf[3])
      
      return speed


    #
    #
    #
    def readDirection(self, motor_id:int) -> int:

      buf:bytes = self.i2c.readfrom_mem(
        MaqueenDrive.Maqueen_I2C_DevAddr, 
        MaqueenDrive.LEFT_MOTOR_REGISTER, 4)

      if (motor_id == MaqueenDrive.Motor_Left):
        return buf[0];

      elif (motor_id == MaqueenDrive.Motor_Right):
        return buf[2];
    
    
