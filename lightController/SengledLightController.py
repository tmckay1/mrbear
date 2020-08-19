from .BaseLightController import BaseLightController

class SengledLightController(BaseLightController):

  def turnOnColor(self,color):
    color = self._colors.get_color(color)