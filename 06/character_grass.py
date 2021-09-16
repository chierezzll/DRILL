from pico2d import *
import math

open_canvas()

grass  = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
while(1):
    while x < 800:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, 90)
        x += 4
        delay(0.01)

    while y < 570:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        y += 4
        delay(0.01)

    while x > 0:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        x -= 4
        delay(0.01)

    while y > 90:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        y -= 4
        delay(0.01)

    while x < 400:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        x += 4
        delay(0.01)



close_canvas()
