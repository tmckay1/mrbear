from ledController.BiblioPixelLedController import BiblioPixelLedController
from colors.BiblioPixelColors import BiblioPixelColors

from bibliopixel.drivers.PiWS281X import PiWS281X

# init led controller
numLeds        = 35   # number of ambient leds
threadedUpdate = True # update color in another thread
colors         = BiblioPixelColors()
driver         = PiWS281X(numLeds)
ledController  = BiblioPixelLedController(colors, driver)
ledController.turnOnColor("red")
sleep(4)
ledController.turnOff()
sleep(4)
ledController.turnOnColor("red")
sleep(4)

# Create listener object that will listen for certain phrases