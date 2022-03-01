import pygame

class Sound:
    def __init__(self, path):
        self.sound = pygame.mixer.Sound(path)

    def getSound(self):
        return self.sound

    def play(self):
        self.sound.play()