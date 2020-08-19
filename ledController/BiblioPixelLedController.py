from bibliopixel.animation.Fill import Fill
from bibliopixel.animation.Off import Off

# control the ambient leds around the personality
class BiblioPixelLedController(object):

  # colors object
  _colors = None

  # bibliopixel animation for the leds
  _led = None

  def __init__(self, colors, led):
    super(object, self).__init__()
    self._colors = colors
    self._led = led

  def turnOff(self):
    anim = Off(self._led)
    anim.run()

  def turnOnColor(self, color):
    bibColor = self._colors.get_color(color)
    anim = Fill(self._led, color = bibColor)
    anim.run()
