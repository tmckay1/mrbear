from .BaseParser import BaseParser

class NameParser(BaseParser):

  # name object that contains all names
  _names = None

  def __init__(self, names):
    super(object, self).__init__()
    self._names = names

  def _parse(self, audio):
    return self._names.extract_name(audio)