from .BaseParser import BaseParser

class SummonParser(BaseParser):

  def _parse(self, audio):
    return ("mr. bear i summon you" in audio) or ("Mr bear i summon you" in audio) or ("mister bear i summon you" in audio) or ("hello mr. bear" in audio) or ("hello Mr bear" in audio) or ("hello mister bear" in audio)