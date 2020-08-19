from .BaseVoiceListener import BaseVoiceListener

class SummonListener(BaseVoiceListener):

  def audioRecognized(self, audio):
    print("Sphinx thinks you said " + audio)

  def audioUnrecognized(self):
    print("Sphinx could not understand audio")

  def requestError(self, e):
    print("Sphinx error; {0}".format(e))