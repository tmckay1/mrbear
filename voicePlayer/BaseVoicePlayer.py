import pygame

class BaseVoicePlayer(object):

  def __init__(self):
    super(object, self).__init__()

  def play_audio(self, audioFilePath):
    print("trying to play " + audioFilePath)
    pygame.mixer.init()
    pygame.mixer.music.load(audioFilePath)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
