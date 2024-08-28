from mbits.lib.MaqueenDrive import MaqueenDrive
from machine import I2C
i2c = I2C(1)   
drive = MaqueenDrive(i2c)
drive.forward(50)

