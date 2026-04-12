from luma.core.interface.serial import i2c
from luma.oled.device import sh1106  # if this fails, swap to ssd1306
from PIL import Image, ImageSequence
from playsound import playsound
import time
# connect to OLED
serial = i2c(port=1, address=0x3C)
device = sh1106(serial)

# create FULL white image
playsound('../Sounds/monotheater.mp3')
background = Image.new("RGBA", (device.width, device.height))
gif = Image.open("../Pictures/monokuma-danganronpa.gif")
posn = (25,0)
while True:
   for frame in ImageSequence.Iterator(gif):
    background = Image.new("RGBA", (device.width,device.height))
    background.paste(frame.resize((device.width-50,device.height),resample=Image.HAMMING),posn)
    device.display(background.convert(device.mode))
    time.sleep(0.5)
