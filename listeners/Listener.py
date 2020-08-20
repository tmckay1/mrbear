import speech_recognition as sr

class Listener(object):

  # parser that knows how to parse audio strings
  _parser = None

  def __init__(self, parser):
    super(object, self).__init__()
    self._parser = parser

  def listen(self):
    while True:
      # obtain audio from the microphone
      r = sr.Recognizer()
      with sr.Microphone() as source:
          print("Say something!")
          audio = r.listen(source)

      # recognize speech using google
      try:
        audio = r.recognize_google(audio)
        data = self.audio_recognized(audio)
        if data:
          return data
      except sr.UnknownValueError:
        if self.audio_unrecognized():
          return None
      except sr.RequestError as e:
        if self.request_error(e)
          return None

  def audio_recognized(self, audio):
    print("recognized audio as " + audio)
    self._parser.parse(audio)

  def audio_unrecognized(self):
    print("could not recognize audio")
    return False

  def request_error(self, e):
    print("encountered request error")
    return False