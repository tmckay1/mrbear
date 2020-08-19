from .BaseListener import BaseListener

class SummonListener(BaseListener):

  def audioRecognized(self, audio):
    print("Google thinks you said " + audio)

  def audioUnrecognized(self):
    print("Google could not understand audio")

  def requestError(self, e):
    print("Google error; {0}".format(e))