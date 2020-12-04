from pico2d import *
import gfw

import main_state
import Player

class Effect():
    image = [None, None, None, None, None, None, None, None, None]

    def __init__(self, x, y, imageX, imageY, sizeX, sizeY, maxFrame, index, speed=1):
        self.x, self.y = x, y
        self.speed = speed
        self.radius = 7.5
        self.imageX, self.imageY, self.sizeX, self.sizeY, self.maxFrame = imageX, imageY, sizeX, sizeY, maxFrame
        self.imageIndex = index
        self.currFrame = 0
        self.isDead = False
        if Effect.image[0] is None:
            Effect.image[0] = load_image('res/Effect_1.png')
        if Effect.image[1] is None:
            Effect.image[1] = load_image('res/ExploS.png')
        if Effect.image[2] is None:
            Effect.image[2] = load_image('res/PowerUp.png')
        if Effect.image[3] is None:
            Effect.image[3] = load_image('res/BombUp.png')
        if Effect.image[4] is None:
            Effect.image[4] = load_image('res/ExploS2.png')
        if Effect.image[5] is None:
            Effect.image[5] = load_image('res/Player_Expol.png')
        if Effect.image[6] is None:
            Effect.image[6] = load_image('res/ExploL.png')
        if Effect.image[7] is None:
            Effect.image[7] = load_image('res/Scarab_Expol.png')
        if Effect.image[8] is None:
            Effect.image[8] = load_image('res/Boss_Expol.png')

    def update(self):
        self.currFrame = (self.currFrame + gfw.delta_time * self.maxFrame * self.speed)
        if self.currFrame >= self.maxFrame:
            self.currFrame = 0
            self.remove()

    def draw(self):
        self.image[self.imageIndex].clip_draw(int(self.currFrame) * self.imageX, 0, self.imageX, self.imageY,
                                              self.x, self.y, self.sizeX, self.sizeY)

    def remove(self):
        gfw.world.remove(self)