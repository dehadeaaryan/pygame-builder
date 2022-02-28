import os
import pygame

class Element:
    def __init__(self, image, screen : pygame.Surface, centerPosition = [0, 0], speed = [0, 0]):
        
        os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

        self.image = image
        self.element = pygame.image.load(self.image)
        self.rect = self.element.get_rect()
        self.speed = speed
        self.screen = screen
        self.center = centerPosition
        self.initialBlit = True
        self.movementAmount = 1
        self.stayInBoundsVar = False

    def getElementRectLeft(self):
        return self.rect.left
    
    def getElementRectRight(self):
        return self.rect.right
    
    def getElementRectTop(self):
        return self.rect.top
    
    def getElementRectBottom(self):
        return self.rect.bottom

    def isOutOfScreenLeft(self):
        if self.getElementRectLeft() < 0:
            return True
        return False
    
    def isOutOfScreenRight(self):
        if self.getElementRectRight() > self.screen.get_width():
            return True
        return False
    
    def isOutOfScreenX(self):
        if self.isOutOfScreenLeft() or self.isOutOfScreenRight():
            return True
        return False
    
    def isOutOfScreenTop(self):
        if self.getElementRectTop() < 0:
            return True
        return False
    
    def isOutOfScreenBottom(self):
        if self.getElementRectBottom() > self.screen.get_height():
            return True
        return False
    
    def isOutOfScreenY(self):
        if self.isOutOfScreenTop() or self.isOutOfScreenBottom():
            return True
        return False
    
    def isInBounds(self):
        if self.isOutOfScreenX() or self.isOutOfScreenY():
            return False
        return True
    
    def stayInBounds(self):
        self.stayInBoundsVar = True
        if self.isOutOfScreenLeft():
            self.rect.left = 0
        if self.isOutOfScreenRight():
            self.rect.right = self.screen.get_width()
        if self.isOutOfScreenTop():
            self.rect.top = 0
        if self.isOutOfScreenBottom():
            self.rect.bottom = self.screen.get_height()
    
    def getSpeed(self):
        return self.speed
    
    def setSpeed(self, x, y):
        self.speed = [x, y]
        return self
    
    def reverseSpeedX(self):
        self.setSpeed(-self.getSpeed()[0], self.getSpeed()[1])
    
    def reverseSpeedY(self):
        self.setSpeed(self.getSpeed()[0], -self.getSpeed()[1])
    
    def move(self):
        self.rect = self.rect.move(self.speed)
    
    def moveWithSpeed(self, speed):
        rect = self.rect
        self.rect = self.rect.move(speed)

        if self.stayInBoundsVar:
            if not self.isInBounds():
                self.stayInBounds()
            else:
                rect = self.rect
        else:
            rect = self.rect
        return rect
    
    def moveUp(self, amount = 1):
        self.rect = self.moveWithSpeed([0, -amount])
    
    def moveDown(self, amount = 1):
        self.rect = self.moveWithSpeed([0, amount])
    
    def moveLeft(self, amount = 1):
        self.rect = self.moveWithSpeed([-amount, 0])
    
    def moveRight(self, amount = 1):
        self.rect = self.moveWithSpeed([amount, 0])
    
    def show(self):
        if self.initialBlit:
            self.rect.center = self.center
            self.screen.blit(self.element, self.rect)
            self.initialBlit = False
        self.screen.blit(self.element, self.rect)
    

    def bouncingAnimaton(self):
        self.move()
        if self.isOutOfScreenX():
            self.reverseSpeedX()
        if self.isOutOfScreenY():
            self.reverseSpeedY()