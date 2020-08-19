from ledController.BiblioPixelLedController import BiblioPixelLedController
from colors.BiblioPixelColors import BiblioPixelColors

from bibliopixel.drivers.PiWS281X import PiWS281X
from bibliopixel.layout.strip import Strip

# init led controller
numLeds        = 35   # number of ambient leds
threadedUpdate = True # update color in another thread
colors         = BiblioPixelColors()

driver         = PiWS281X(numLeds)
led            = Strip(driver, threadedUpdate)
ledController  = BiblioPixelLedController(colors, led)
ledController.turnOnColor("red")
sleep(4)

# Create listener object that will listen for certain phrases