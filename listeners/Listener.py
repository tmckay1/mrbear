import speech_recognition as sr

class Listener(object):

  # parser that knows how to parse audio strings
  _parser = None

  def __init__(self, parser):
    super(object, self).__init__()
    self._parser = parser

  def listen(self):
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # recognize speech using google
    try:
      audio = r.recognize_google(audio)
      return self.audio_recognized(audio)
    except sr.UnknownValueError:
      return self.audio_unrecognized()
    except sr.RequestError as e:
      return self.request_error(e)

  def audio_recognized(self, audio):
    print("recognized audio as " + audio)
    return self._parser.parse(audio)

  def audio_unrecognized(self):
    print("could not recognize audio")
    return None

  def request_error(self, e):
    print("encountered request error")
    return None