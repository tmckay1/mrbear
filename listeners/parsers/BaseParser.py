class BaseParser(object):

  def parse(self, audio):
    print("in class " + str(self.__class__.__name__))
    return self._parse(audio.lower())