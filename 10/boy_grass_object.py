from pico2d import *
import random

BOTTOM = 50
# Game object class here

class Ball():
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x = random.randint(0, 800)
        self.y = 599
        self.v = random.randint(5, 15)

    def update(self):
        self.y -= self.v
        if self.y < BOTTOM:
            self.y = 50

    def draw(self):
        self.image.draw(self.x, self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

grass = Grass()
running = True


balls = [Ball() for i in range(20)]
# game main loop code
while running:
    handle_events()
    clear_canvas()
    grass.draw()
    for ball in balls:
        ball.draw()
    for ball in balls:
        ball.update()
    update_canvas()
    delay(0.05)

# finalization code