from ledController.BiblioPixelLedController import BiblioPixelLedController
from colors.BiblioPixelColors import BiblioPixelColors

from bibliopixel.drivers.PiWS281X import PiWS281X
from bibliopixel.layout.strip import Strip

numLeds       = 35
colors        = BiblioPixelColors()
driver        = PiWS281X(numLeds)
led           = Strip(driver)
ledController = BiblioPixelLedController(colors, led)
ledController.turnOn("red")
sleep(4)

# Create listener object that will listen for certain phrases