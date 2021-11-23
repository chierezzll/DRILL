import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from bird import Bird
from ball import Ball

name = "MainState"

boy = None
grass = None
balls = []
big_balls = []



def collide(a, b):
    # fill here
    return True




def enter():
    global boy, bird, bird2, bird3, bird4, bird5
    boy = Boy()
    bird = Bird(random.randint(0, 1600), random.randint(300,500), 2, 1, 3)
    bird2 = Bird(random.randint(0, 1600), random.randint(300,500), 2, 1, 3)
    bird3 = Bird(random.randint(0, 1600), random.randint(300,500), 2, 1, 3)
    bird4 = Bird(random.randint(0, 1600), random.randint(300,500), 2, 1, 3)
    bird5 = Bird(random.randint(0, 1600), random.randint(300,500), 2, 1, 3)
    game_world.add_object(boy, 1)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)

    # fill here for balls





def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    bird.update()
    bird2.update()
    bird3.update()
    bird4.update()
    bird5.update()
    for game_object in game_world.all_objects():
        game_object.update()

    # fill here for collision check



def draw():
    clear_canvas()
    bird.draw()
    bird2.draw()
    bird3.draw()
    bird4.draw()
    bird5.draw()

    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






