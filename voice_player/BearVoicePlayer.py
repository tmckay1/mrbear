from .BaseVoicePlayer import BaseVoicePlayer

class BearVoicePlayer(BaseVoicePlayer):

  # path to generic audio tracks
  _audio_repo = "../bear_sounds/"

  def play_ending(self, name):
    self._play_ending_part1(1)
    self._play_ending_part2(name)
    self._play_ending_part3(1)

  def play_hello(self, index):
    path = self._audio_repo + "start/hello" + str(index) + ".mp3"
    self.play_audio(path)

  def play_intro(self, name, index):
    path = self._audio_repo + "intros/" + name + "intro" + str(index) + ".mp3"
    self.play_audio(path)

  def play_error(self, index):
    path = self._audio_repo + "error/error" + str(index) + ".mp3"
    self.play_audio(path)

  def play_retry(self, index):
    path = self._audio_repo + "retry/error" + str(index) + ".mp3"
    self.play_audio(path)

  def play_wake_up(self, index):
    path = self._audio_repo + "wakingup/wakeup" + str(index) + ".mp3"
    self.play_audio(path)

  def play_welcome(self, index):
    path = self._audio_repo + "welcome/welcome" + str(index) + ".mp3"
    self.play_audio(path)

  def _play_ending_part1(self, index):
    path = self._audio_repo + "ending/intro" + str(index) + ".mp3"
    self.play_audio(path)

  def _play_ending_part2(self, name):
    self._play_name(name)

  def _play_ending_part3(self, index):
    path = self._audio_repo + "ending/winner" + str(index) + ".mp3"
    self.play_audio(path)

  def _play_name(self, name):
    path = self._audio_repo + "names/" + name + ".mp3"
    self.play_audio(path)