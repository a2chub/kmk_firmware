from board import *
from busio import I2C

i2c = I2C(GP15, GP14)

while not i2c.try_lock():
    pass

print('addr 0x{0:x}'.format(i2c.scan()[0]))
print('addr 0x{0:x}'.format(i2c.scan()[1]))
i2c.deinit()