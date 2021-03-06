from .BaseParser import BaseParser

class ActionParser(BaseParser):

  # name object that contains all names
  _names = None

  # actions object that contains all actions
  _actions = None

  def __init__(self, names, actions):
    super(object, self).__init__()
    self._names = names
    self._actions = actions

  def _parse(self, audio):
    action = self._parse_action_from_audio(audio)
    if action == "dispute":
      return self._parse_names_from_audio(audio)
    else:
      return None

  def _parse_action_from_audio(self, audio):
    return self._actions.extract_action(audio)

  def _parse_names_from_audio(self, audio):
    print(" audio " + str(audio))
    return self._names.extract_names(audio)