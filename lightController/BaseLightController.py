# create a method to send commands to an API
class BaseLightController(object):

  # colors object
  _colors = None

  # api that controls lighting
  _api = None

  def __init__(self, colors, api):
    super(object, self).__init__()
    self._colors = colors
    self._api = api

  def turnOnColor(self,color):
    pass
