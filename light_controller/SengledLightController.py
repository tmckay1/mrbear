from .BaseLightController import BaseLightController

class SengledLightController(BaseLightController):

  def turn_on_color(self, color):
    color = self._colors.get_color(color)
    self._api.set_color(self._lights, color)

  def turn_off(self):
    self._api.set_off(self._lights)