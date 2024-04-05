import time
from relay import turnOff, turnOn, turnOnForAsync


for i in range(8):
    turnOn(i)
    time.sleep(0.1)


for i in range(8):
    turnOff(i)
    time.sleep(0.1)


for i in range(8):
    turnOnForAsync(i, 1)
