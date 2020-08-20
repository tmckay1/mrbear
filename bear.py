from ledController.BiblioPixelLedController import BiblioPixelLedController
from colors.BiblioPixelColors import BiblioPixelColors
from lightController.SengledLightController import SengledLightController
from colors.SengledColors import SengledColors
from scripts.BearScript import BearScript

from bibliopixel.drivers.PiWS281X import PiWS281X

import sengled

# init led controller
numLeds        = 35
colors         = BiblioPixelColors()
driver         = PiWS281X(numLeds)
led_controller  = BiblioPixelLedController(colors, driver)

# init lighting controller
api = sengled.api_from_env()
colors = SengledColors()
colored_lights = api.filter_colored_lamps()
living_room_lights = list(filter(lambda x: ("LivingRoom" in x.name), colored_lights))
light_controller = SengledLightController(colors, api, colored_lights)

# run script
script = BearScript(led_controller, light_controller)
script.run()
