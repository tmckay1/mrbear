from .BaseVoicePlayer import BaseVoicePlayer

class BearVoicePlayer(BaseVoicePlayer):

  # path to generic audio tracks
  _audio_repo = "../../bear_sounds/"

  def playEnding(self, name):
    self._playEndingPart1(1)
    self._playEndingPart2(name)
    self._playEndingPart3(1)

  def _playEndingPart1(self, index):
    path = self._audio_repo + "ending/intro" + index + ".mp3"
    self.playAudio(path)

  def _playEndingPart2(self, name):
    self.playName(name)

  def _playEndingPart3(self, index):
    path = self._audio_repo + "ending/winner" + name + ".mp3"
    self.playAudio(path)

  def playIntro(self, name, index):
    path = self._audio_repo + "intros/" + name + "intro" + index + ".mp3"
    self.playAudio(path)

  def playName(self, name):
    path = self._audio_repo + "names/" + name + ".mp3"
    self.playAudio(path)

  def playWakeUp(self, index):
    path = self._audio_repo + "wakingup/wakeup" + index + ".mp3"
    self.playAudio(path)