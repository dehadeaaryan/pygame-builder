# pygame-builder
 
### Introduction
Use this package to create a game in python in just a few lines of code. Built on top of Pygame, this module is perfect for beginners looking to make their first game. Experts may also find this useful when trying to save time. Enjoy!

### Code Format
```Python
from pygame_builder import Pygame, Element, Image

with Pygame(backgroundImage : Image = image, size : list = [480, 270], windowCaption = "Pygame", fps = 60, backgroundColour : tuple = (0, 0, 0), backgroundMusic : Music = None), backgroundSound = None) as pg:
    element = Element(image : Image, parent, centerPosition = [0, 0], speed = [1, 1])
    pg.add(element)
    pg.loop(lambda : <callable>)
```

### Example
```Python
from pygame_builder import Pygame, Element, Image

ballGif = "/path/to/ball.gif"

def main():
	ball.bouncingAnimation()

with Pygame() as pg:
    ball = Element(Image(ballGif), pg, pg.getScreenCenter(), [2, 2])
    pg.add(ball)
    pg.loop(lambda : main)
```