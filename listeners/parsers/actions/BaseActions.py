# base actions object to be overriden by subclasses, contains names of all actions
class BaseActions(object):

  ACTIONS = []

  def extract_action(self, audio):
    actions = []
    for action in self.get_actions():
      if action in audio:
        actions.append(action)

    # only return 1 action
    return actions[0] if len(actions) == 1 else None

  def get_actions(self):
    return self.ACTIONS