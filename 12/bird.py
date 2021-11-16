import game_framework
from pico2d import *
import game_world

PIXEL_PER_METER = (10.0 / 0.3)
BIRD_SPEED_KMPH = 100.0
BIRD_SPEED_MPM = (BIRD_SPEED_KMPH * 1000.0 / 60.0)
BIRD_SPEED_MPS = (BIRD_SPEED_MPM / 60.0)
BIRD_SPEED_PPS = (BIRD_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:

    def __init__(self, x, y, d, num, velocity):
        self.image = load_image('bird100x100x14.png')
        self.x = x
        self.y = y
        self.velocity = velocity
        self.d = d  # 이동범위
        self.dir = 1
        self.num = num  # 갯수
        self.frame = 0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14   # 새의 애니메이션 시트에 있는 14개의 프레임을 초당 2개의 프레임을 보여주도록 구현했습니다.
        self.x += self.velocity * self.dir
        if self.x >= 1600:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1


    def draw(self):
            self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y, 100, 100) # 1프레임당 3cm로 잡았으며 새의 크기는 가로 세로 100프레임. 즉, 가로 세로 300cm이다

