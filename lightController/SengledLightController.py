from .BaseLightController import BaseLightController

class SengledLightController(BaseLightController):

  def turnOnColor(self, color):
    color = self._colors.get_color(color)
    self._api.set_color(self._lights, color)

  def turnOff(self):
    self._api.set_off(self._lights)