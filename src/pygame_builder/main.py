import os
import sys, pygame

from PIL import Image as PILImage
import requests

from .element import Element
from .image import Image
from .sound import Sound
from .music import Music

imgUrl = "https://raw.githubusercontent.com/dehadeaaryan/pygame-builder/main/pygame-builder.png"
img = PILImage.open(requests.get(imgUrl, stream=True).raw)
raw = img.tobytes("raw", "RGB")
image = pygame.image.fromstring(raw, [480, 270], "RGB")

class Pygame:
    def __init__(self, backgroundImage : Image = image, size : list = [480, 270], windowCaption = "Pygame", fps = 60, backgroundColour : tuple = (0, 0, 0), backgroundMusic : Music = None):
        
        os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
        
        pygame.init()

        self.size = self.width, self.height = size
        self.fps = fps
        self.windowCaption = windowCaption
        if backgroundImage != image:
            self.backgroundImage = backgroundImage.getImage()
        else:
            self.backgroundImage = image
        self.backgroundColour = backgroundColour

        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(windowCaption)
        self.clock = pygame.time.Clock()
        self.mixer = pygame.mixer
        self.music = self.mixer.music
        self.time = pygame.time

        self.elements = []
        self.main = None
        self.keyboardEnabled = False
        self.backgroundMusic = None

        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.movingElement = None
        self.movementAmount = 1
        self.stayInBounds = None

        self.background = self.backgroundImage
        self.background = pygame.transform.scale(self.background, size)
        self.mixer.init()
        if backgroundMusic:
            self.backgroundMusic = backgroundMusic

    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.run()
    
    def __add__(self, element : Element):
        self.add(element)
        return self



    
    def getScreen(self):
        return self.screen
    
    def getScreenWidth(self):
        return self.width
    
    def getScreenHeight(self):
        return self.height
    
    def getScreenCenter(self):
        return self.width // 2, self.height // 2
    
    def add(self, element : Element):
        self.elements.append(element)
    
    def loop(self, loop : callable):
        self.main = loop
    
    def addKeyboardMovement(self, element : Element, amount, up, down, left, right, stayInBounds = True):
        if not self.movingElement:
            self.movementAmount = amount
            self.keyboardEnabled = True
            self.movingElement = element
            self.movingElement.movementAmount = amount
            self.stayInBounds = stayInBounds
            self.up = True if up else False
            self.down = True if down else False
            self.left = True if left else False
            self.right = True if right else False
    
    def run(self):
        if not self.main:
            print("No loop defined. Set one with loop(YOUR_LOOP_HERE)")
            return
        
        if self.backgroundMusic:
            self.backgroundMusic.play()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                if self.keyboardEnabled and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                
            if self.keyboardEnabled:
                keyPressed = pygame.key.get_pressed()

                if self.stayInBounds:
                    self.movingElement.stayInBounds()
                
                if self.up and keyPressed[pygame.K_UP]:
                    self.movingElement.moveUp(self.movementAmount)
                if self.down and keyPressed[pygame.K_DOWN]:
                    self.movingElement.moveDown(self.movementAmount)
                if self.left and keyPressed[pygame.K_LEFT]:
                    self.movingElement.moveLeft(self.movementAmount)
                if self.right and keyPressed[pygame.K_RIGHT]:
                    self.movingElement.moveRight(self.movementAmount)
            
            self.main()
            
            self.screen.fill(self.backgroundColour)
            self.screen.blit(self.background, (0, 0))

            for element in self.elements:
                element.show()
            
            self.clock.tick(self.fps)
            pygame.display.update()