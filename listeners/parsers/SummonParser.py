from .BaseParser import BaseParser

class SummonParser(BaseParser):

  def _parse(self, audio):
    print("parsing summon audio '" + audio + "'")
    print("is summoned: " + str("mr. bear i summon you" in audio))
    return "mr. bear i summon you" in audio