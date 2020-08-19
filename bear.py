from ledController.BiblioPixelLedController import BiblioPixelLedController
from colors.BiblioPixelColors import BiblioPixelColors
from lightController.SengledLightController import SengledLightController
from colors.SengledColors import SengledColors
from voicePlayer.BearVoicePlayer import BearVoicePlayer
from listeners.SummonListener import SummonListener

from bibliopixel.drivers.PiWS281X import PiWS281X

import sengled 

# init led controller
numLeds        = 35
colors         = BiblioPixelColors()
driver         = PiWS281X(numLeds)
ledController  = BiblioPixelLedController(colors, driver)

# init lighting controller
api = sengled.api_from_env()
colors = SengledColors()
colored_lights = api.filter_colored_lamps()
living_room_lights = list(filter(lambda x: ("LivingRoom" in x.name), colored_lights))
lightController = SengledLightController(colors, api, colored_lights)

# init voice player
voicePlayer = BearVoicePlayer()

# init listener and listen
listener = SummonListener()
listener.listen()