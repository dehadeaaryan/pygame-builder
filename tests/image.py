import pygame

class Image:
    def __init__(self, path):
        self.image = pygame.image.load(path)

    def getWidth(self):
        return self.image.get_width()
    
    def getHeight(self):
        return self.image.get_height()
    
    def getCenter(self):
        return self.getWidth() // 2, self.getHeight() // 2
    
    def getRect(self):
        return self.image.get_rect()
    
    def scale(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))
        return self.image
    
    def getImage(self):
        return self.image