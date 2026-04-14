from gpiozero import OutputDevice
import time
motorPins = (12,16,20,21)
motors = list(map(lambda pin: OutputDevice(pin), motorPins))
while True:
    for i in (0,3,1):
        if i>=1:
            motors[i-1].off()
            motors[i].on()
        else:
            motors[3].off()
            motors[i].on()
        time.sleep(2)