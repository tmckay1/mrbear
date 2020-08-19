# base color object to control specific lights
class BaseColors(object):

  COLORS = {}

  def get_color(self, color):
    return self.COLORS[color]

  def get_colors(self):
    return self.COLORS

  def get_default_color(self):
    return self.get_color("red")