import speech_recognition as sr

class BaseListener(object):

  def __init__(self):
    super(object, self).__init__()

  def listen(self):
    while True:
      # obtain audio from the microphone
      r = sr.Recognizer()
      with sr.Microphone() as source:
          print("Say something!")
          audio = r.listen(source)

      # recognize speech using Sphinx
      try:
        audio = r.recognize_sphinx(audio)
        self.audioRecognized(audio)
      except sr.UnknownValueError:
        self.audioUnrecognized()
      except sr.RequestError as e:
        self.requestError(e)

  def audioRecognized(self, audio):
    pass

  def audioUnrecognized(self):
    pass

  def requestError(self, e):
    pass