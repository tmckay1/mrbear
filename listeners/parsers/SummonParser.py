from .BaseParser import BaseParser

class SummonParser(BaseParser):

  def _parse(self, audio):
    return "mr. bear i summon you" in audio