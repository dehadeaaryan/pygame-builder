# pygame-builder
 
### Introduction
Use this package to create a game in python in just a few lines of code. Built on top of Pygame, this module is perfect for beginners looking to make their first game. Experts may also find this useful when trying to save time. Enjooy!

### Code Format
```Python
from pygame_builder import Pygame, Element

with Pygame(backgroundImage = image, size = [480, 270], windowCaption = "Pygame", fps = 60, backgroundColour = (0, 0, 0), backgroundSound = None) as pg:
    element = Element(image, screen : pygame.Surface, centerPosition = [0, 0], speed = [0, 0])
    pg.add(element)
    pg.loop(lambda : element.bouncingAnimation())
```