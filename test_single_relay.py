import time
from relay import turnOff, turnOn, turnOnForAsync


turnOn(4)
time.sleep(1)
turnOff(4)


turnOn(5)
time.sleep(1)
turnOff(5)


turnOnForAsync(4, 1)
turnOnForAsync(4, 1)
time.sleep(1)
