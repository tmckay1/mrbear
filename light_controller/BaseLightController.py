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

  def turn_on_color(self, color):
    pass
