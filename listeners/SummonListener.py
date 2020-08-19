from .BaseListener import BaseListener

class SummonListener(BaseListener):

  def audioRecognized(self, audio):
    print("Sphinx thinks you said " + audio)

  def audioUnrecognized(self):
    print("Sphinx could not understand audio")

  def requestError(self, e):
    print("Sphinx error; {0}".format(e))