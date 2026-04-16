from gpiozero import OutputDevice
from time import sleep

IN1 = OutputDevice(12)
IN2 = OutputDevice(16)
IN3 = OutputDevice(20)
IN4 = OutputDevice(21)

pins = [IN1, IN2, IN3, IN4]

# Base sequence
seq = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

def stepmotor(steps, direction="CW", delay=0.003):
    sequence = seq if direction == "CW" else list(reversed(seq))

    for _ in range(steps):
        for step in sequence:
            for pin, state in zip(pins, step):
                if state:
                    pin.on()
                else:
                    pin.off()
            sleep(delay)

try:
    stepmotor(512, direction="CW")   # change to "CCW" if needed
finally:
    for pin in pins:
        pin.off()
