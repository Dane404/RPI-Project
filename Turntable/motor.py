from gpiozero import OutputDevice
import time
motorPins = (12,16,20,21)

motors = list(map(lambda pin: OutputDevice(pin),motorPins))
while True:
    for i in range(0,4,1):
        motors(i).on
        