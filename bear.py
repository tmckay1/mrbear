from ledController.BiblioPixelLedController import BiblioPixelLedController
from colors.BiblioPixelColors import BiblioPixelColors
from lightController.SengledLightController import SengledLightController
from colors.SengledColors import SengledColors
from voicePlayer.BearVoicePlayer import BearVoicePlayer
from listeners.SummonListener import SummonListener
from listeners.parsers.SummonParser import SummonParser
from listeners.parsers.NameParser import NameParser
from listeners.parsers.ActionParser import ActionParser
from listeners.parsers.names.AllNames import AllNames
from listeners.parsers.actions.BearActions import BearActions

from bibliopixel.drivers.PiWS281X import PiWS281X

import sengled

import random

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
voice_player = BearVoicePlayer()

while True:
  # listen for summon call
  parser = SummonParser()
  listener = SummonListener(parser)

  is_summoned = listener.listen()
  if is_summoned:
    print("we are summoned")
    # wake up
    total_wake_ups = 8
    wake_up_index = random.randint(1, total_wake_ups)
    voice_player.playWakeUp(wake_up_index)

    # listen for names
    all_names = AllNames()
    name_parser = NameParser(all_names)
    listener = NameListener(name_parser)
    name = listener.listen()

    # if we get the name continue, otherwise retry once
    if name:
      print(name + " is speaking")
      # play name recognition
      total_name_recordings = 8
      name_recording_index = random.randint(1, total_name_recordings)
      voice_player.play_intro(name, name_recording_index)

      # listen for action]
      actions = BearActions()
      action_parser = ActionParser(all_names, actions)
      listener = ActionListener(action_parser)
      names = listener.listen()

      # if we get the names continue, otherwise retry once
      if names:
        print("The names are " + str(names))
        winner = all_names.pick_winner(names)
        print("The winner is " + winner)
        voice_player.play_ending(name)
      else:
        print("unrecognizable action")

    else:
      print("unrecognizable name")
  else:
    print("is not summoned")


