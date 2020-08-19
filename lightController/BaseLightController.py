# create a method to send commands to an API
class BaseLightController(object):

  # colors object
  _colors = None

  # api that controls lighting
  _api = None

  # array of lights to control
  _lights = []

  def __init__(self, colors, api, lights):
    super(object, self).__init__()
    self._colors = colors
    self._api = api
    self._lights = lights

  def turnOnColor(self, color):
    pass
