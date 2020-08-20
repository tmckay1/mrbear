from .Listener import Listener

class NameListener(Listener):

  def audio_unrecognized(self):
    return True

  def request_error(self, e):
    return True