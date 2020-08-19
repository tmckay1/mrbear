from ledController.BiblioPixelLedController import BiblioPixelLedController
from colors.BiblioPixelColors import BiblioPixelColors

from bibliopixel.drivers.PiWS281X import PiWS281X
import time

# init led controller
numLeds        = 35   # number of ambient leds
threadedUpdate = True # update color in another thread
colors         = BiblioPixelColors()
driver         = PiWS281X(numLeds)
ledController  = BiblioPixelLedController(colors, driver)
ledController.turnOnColor("red")
time.sleep(4)
ledController.turnOff()
time.sleep(4)
ledController.turnOnColor("blue")
time.sleep(4)
ledController.turnOff()

# Create listener object that will listen for certain phrases