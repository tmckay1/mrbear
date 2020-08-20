from .Listener import Listener

class ActionListener(Listener):

  def audio_unrecognized(self):
    return True

  def request_error(self, e):
    return True