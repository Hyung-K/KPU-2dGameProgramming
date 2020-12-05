from pico2d import *
import gfw

import Effect
import random
import math
import SoundM

class Blue_Bullet2:
    image = None

    def __init__(self, x, y, number, deltaX, deltaY):
        self.number = number
        self.x, self.y = x, y
        self.deltaX, self.deltaY = deltaX, deltaY
        self.radius = 10
        self.isDead = False
        self.frame = 0
        self.Sound = SoundM
        self.lifeTime = random.randint(100, 300) / 100
        self.deathTime = 0
        self.index = 0
        if Blue_Bullet2.image is None:
            Blue_Bullet2.image = load_image('res/Blue_Bullet2.png')

    def Bullet_LifeTime(self):
        if self.isDead is True or self.y <= 0 or self.x < 0 or self.x > 720:
            self.remove()

    def update(self):
        self.Bullet_LifeTime()
        self.x += gfw.delta_time * self.deltaX * 2
        self.y += gfw.delta_time * self.deltaY * 2

        self.frame += gfw.delta_time * 10
        if self.frame >= 16:
            self.frame = 0
        if self.isDead is True or self.y <= 0 or self.x < -10 or self.x > 740:
            if self.number > 0:
                self.Sound.playSound(12, 40)
                bEf = Effect.Effect(self.x, self.y, 80, 80, 100, 100, 10, 7, 0.5)
                gfw.world.add(gfw.layer.Effect, bEf)
                BB = Blue_Bullet2(self.x, self.y, self.number - 1, 0, 100)
                gfw.world.add(gfw.layer.MonsterBullet, BB)
                BB1 = Blue_Bullet2(self.x, self.y,  self.number - 1, 50 * math.sqrt(2), 50 * math.sqrt(2))
                gfw.world.add(gfw.layer.MonsterBullet, BB1)
                BB2 = Blue_Bullet2(self.x, self.y,  self.number-1, 100, 0)
                gfw.world.add(gfw.layer.MonsterBullet, BB2)
                BB3 = Blue_Bullet2(self.x, self.y,  self.number-1, 50 * math.sqrt(2), -50 * math.sqrt(2))
                gfw.world.add(gfw.layer.MonsterBullet, BB3)
                BB4 = Blue_Bullet2(self.x, self.y, self.number-1, 0, -100)
                gfw.world.add(gfw.layer.MonsterBullet, BB4)
                BB5 = Blue_Bullet2(self.x, self.y,  self.number-1, -50 * math.sqrt(2), -50 * math.sqrt(2))
                gfw.world.add(gfw.layer.MonsterBullet, BB5)
                BB6 = Blue_Bullet2(self.x, self.y,  self.number-1, -100, 0)
                gfw.world.add(gfw.layer.MonsterBullet, BB6)
                BB7 = Blue_Bullet2(self.x, self.y,  self.number-1, -50 * math.sqrt(2), 50 * math.sqrt(2))
                gfw.world.add(gfw.layer.MonsterBullet, BB7)
            self.remove()

    def remove(self):
        gfw.world.remove(self)

    def draw(self):
        self.image.clip_draw(450 * int(self.frame), 0, 450, 450, self.x, self.y, 20, 20)
