from main import Pygame, Element, Image
import time

ballGif = "ball.gif"

def main():
    global count
    count += 1
    if ball.detectCollision(collide) and count >= 300:
        pg.remove(collide)
        time.sleep(0.5)
    print(ball.detectCollision(collide), count)

with Pygame() as pg:
    count = 0
    ball = Element(image = Image(ballGif), parent = pg, centerPosition = pg.getScreenCenter(), speed = [2, 2])
    pg.add(ball)
    pygameImage = Image("pygame_tiny.png")
    pygameImage.scale(100, 100)
    collide = Element(pygameImage, parent = pg, centerPosition = (pg.getScreenWidth()//2, 10), speed = [0, 0])
    pg.add(collide)
    pg.addKeyboardMovement(element = ball, amount = 2, up = True, down = True, left = True, right = True)
    pg.loop(main)