class BaseParser(object):

  def parse(self, audio):
    return self._parse(audio.lower())