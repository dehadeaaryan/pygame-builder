import pygame

class Music:
    def __init__(self, path):
        pygame.mixer.music.load(path)
        self.music = pygame.mixer.music
    
    def getMusic(self):
        return self.music
        
    def play(self, loops = -1):
        self.music.play(loops)
        
    def stop(self):
        self.music.stop()