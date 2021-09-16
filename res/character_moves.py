from pico2d import *
import math


open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
j = 270
a = 400 + 200 * math.cos(math.radians(90))
b = 90 + 200 * math.sin(math.radians(90))

while(1):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(400 + 200 * math.cos(math.radians(j)), 290 + 200 * math.sin(math.radians(j)))
    j = j + 2
    
    delay(0.01)

