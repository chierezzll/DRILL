from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # elif event.type == SDL_MOUSEMOTION:
        #     x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
mx, my = random.randrange(0, KPU_WIDTH), random.randrange(0, KPU_HEIGHT)
a = mx - x
b = my - y
dir = 1
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand.draw(mx, my)

    character.clip_draw(frame * 100, 100 * dir, 100, 100, x, y)

    update_canvas()
    frame = (frame + 1) % 8

    if(x < mx and y < my):
        x += 1
        y += 1
    elif(x > mx and y < my):
        x -= 1
        y += 1
        dir = 0
    elif (x > mx and y > my):
        x -= 1
        y -= 1
        dir = 0
    elif (x < mx and y > my):
        x += 1
        y -= 1

    if (x == mx and y == my):
        mx, my = random.randrange(0, KPU_WIDTH), random.randrange(0, KPU_HEIGHT)

    handle_events()

close_canvas()




