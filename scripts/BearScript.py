from voicePlayer.BearVoicePlayer import BearVoicePlayer
from listeners.SummonListener import SummonListener
from listeners.NameListener import NameListener
from listeners.ActionListener import ActionListener
from listeners.parsers.SummonParser import SummonParser
from listeners.parsers.NameParser import NameParser
from listeners.parsers.ActionParser import ActionParser
from listeners.parsers.names.AllNames import AllNames
from listeners.parsers.actions.BearActions import BearActions

class BearScript(object):

  # controller to change led lights
  _led_controller = None

  # controller to change lighting
  _light_controller = None

  # object to play audio
  _voice_player = None

  def __init__(self, led_controller, light_controller):
    super(object, self).__init__()
    self._led_controller = led_controller
    self._light_controller = light_controller
    self._voice_player = BearVoicePlayer()

  def run(self):
    while True:

      # only continue if summoned
      if self.listen_for_summoned():
        self.run_wakeup()
        name = self.listen_for_speaker_name()

        # if we get the name continue, otherwise retry once
        if name:
          self.run_recognize_name()
          names = self.listen_for_action_and_names()

          # if we get the names continue, otherwise retry once
          if names:
            self.run_winner_names(names)
          else:
            print("unrecognizable action")

        else:
          print("unrecognizable name")
      else:
        print("is not summoned")

  def run_wakeup(self):
    total_wake_ups = 8
    wake_up_index = random.randint(1, total_wake_ups)
    voice_player.play_wake_up(wake_up_index)

  def run_recognize_name(self, name):
    # play name recognition
    total_name_recordings = 8
    name_recording_index = random.randint(1, total_name_recordings)
    voice_player.play_intro(name, name_recording_index)

  def run_winner(self, winner):
    winner = all_names.pick_winner(names)
    voice_player.play_ending(winner)

  def listen_for_speaker_name(self):
    all_names = AllNames()
    name_parser = NameParser(all_names)
    listener = NameListener(name_parser)
    return listener.listen()

  def listen_for_action_and_names(self):
    actions = BearActions()
    all_names = AllNames()
    action_parser = ActionParser(all_names, actions)
    listener = ActionListener(action_parser)
    return listener.listen()

  def listen_for_summoned(self):
    parser = SummonParser()
    listener = SummonListener(parser)
    return listener.listen()