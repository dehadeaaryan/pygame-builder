import os
import sys, pygame

from PIL import Image
import requests

imgUrl = "https://raw.githubusercontent.com/dehadeaaryan/pygame-builder/main/pygame-builder.png"
img = Image.open(requests.get(imgUrl, stream=True).raw)
raw = img.tobytes("raw", 'RGBA')
image = pygame.image.fromstring(raw, [480, 270], 'RGBA')

class Pygame:
    def __init__(self, backgroundImage = image, size = [480, 270], windowCaption = "Pygame", fps = 60, backgroundColour = (0, 0, 0), backgroundSound = None):
        
        os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
        
        pygame.init()

        self.size = self.width, self.height = size
        self.fps = fps
        self.windowCaption = windowCaption
        self.backgroundImage = backgroundImage
        self.backgroundColour = backgroundColour

        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(windowCaption)
        self.clock = pygame.time.Clock()
        self.mixer = pygame.mixer
        self.time = pygame.time
        self.music = self.mixer.music

        self.elements = []
        self.main = None
        self.keyboardEnabled = False
        self.backgroundSound = None

        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.movingElement = None
        self.movementAmount = 1
        self.stayInBounds = None

        self.background = pygame.image.load(self.backgroundImage)
        self.background = pygame.transform.scale(self.background, size)
        self.mixer.init()
        if backgroundSound:
            self.mixer.music.load(backgroundSound)
            self.backgroundSound = self.mixer.music

    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.run()
    
    def __add__(self, element):
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
    
    def add(self, element):
        self.elements.append(element)
    
    def loop(self, loop):
        self.main = loop
    
    def addKeyboardMovement(self, element, amount, up, down, left, right, stayInBounds = True):
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
        
        if self.backgroundSound:
            self.backgroundSound.play(-1)

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