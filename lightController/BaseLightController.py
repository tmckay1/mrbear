# create a method to send commands to an API
class BaseLightController(object):

  _colors = None

  def __init__(self, colors):
    super(object, self).__init__()
    self._colors = colors

  def turnOnColor(self,color):
    pass
