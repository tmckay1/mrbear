import random

# base names object to be overriden by subclasses, contains names of all participants
class BaseNames(object):

  # dict with keys that are names given from the parser and values are the actual names we use to store audio tracks
  TRANSLATED_NAMES = {}

  # dict with keys that are the translated names and values that are the weights to see who wins
  WEIGHTED_NAMES = {}

  def get_weight(self, name):
    return self.WEIGHTED_NAMES[name]

  def get_names(self):
    return self.WEIGHTED_NAMES.keys()

  def get_raw_names(self):
    return self.TRANSLATED_NAMES.keys()

  def extract_name(self, audio):
    names = []
    words = audio.split()
    for name in self.get_raw_names():
      if name in words:
        names.append(self.translate_name(name))

    # only return 1 name
    return names[0] if len(names) == 1 else None

  def extract_names(self, audio):
    names = []
    words = audio.split()
    print("extract_names " + str(names))
    print("words" + str(words))
    print("audio " + str(audio))
    print("raw " + str(self.get_raw_names()))
    for name in self.get_raw_names():
      if name in words:
        print("found name " + name)
        names.append(self.translate_name(name))

    print("names again " + str(names))
    # only return 2 names or none
    return names if len(names) == 2 else None

  def pick_winner(self, names):
    total_weight = self.get_weight(names[0]) + self.get_weight(names[1])
    rand_num = random.randint(1, total_weight)
    return names[0] if rand_num <= self.get_weight(names[0]) else names[1]

  def translate_name(self, name):
    return self.TRANSLATED_NAMES[name]