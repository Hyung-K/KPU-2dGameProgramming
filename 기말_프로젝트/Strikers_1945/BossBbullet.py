from pico2d import *

import gfw
import Player
import Bbullet
import Effect
import random
import math


class Boss_Bbullet:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.radius = 25
        self.isdead = False
        self.frame = 0
        self.lifeTime = random.randint(100, 300) / 100
        self.deathTime = 0
        self.index = 0
        self.Number = 0
        self.randomSpeed_Delta = random.randint(30, 50) / 100
        if Boss_Bbullet.image is None:
            Boss_Bbullet.image = load_image('res/Blue_Bullet2.png')
        for player in gfw.world.objects_at(gfw.layer.Player):
            self.deltaX = self.x-player.x
            self.deltaY = self.y-player.y

    def Bullet_LifeTime(self):
        self.deathTime += gfw.delta_time
        if self.deathTime > self.lifeTime:
            self.isdead = True

    def update(self):
        self.Bullet_LifeTime()

        self.x -= self.deltaX * gfw.delta_time * self.randomSpeed_Delta
        self.y -= self.deltaY * gfw.delta_time * self.randomSpeed_Delta
        self.frame += gfw.delta_time * 15

        if self.frame >= 15:
            self.frame = 0
        if self.isdead is True:
            Bf1 = Effect.Effect(self.x, self.y, 80, 80, 100, 100, 10, 7, 0.5)
            gfw.world.add(gfw.layer.Effect, Bf1)
            BBB = Bbullet.Bbullet2(self.x, self.y, self.Number-1, 0, 100)
            gfw.world.add(gfw.layer.MonsterBullet, BBB)
            BBB1 = Bbullet.Bbullet2(self.x, self.y,  self.Number-1, 50 * math.sqrt(2), 50 * math.sqrt(2))
            gfw.world.add(gfw.layer.MonsterBullet, BBB1)
            BBB2 = Bbullet.Blue_Bullet2(self.x, self.y,  self.Number-1, 100, 0)
            gfw.world.add(gfw.layer.MonsterBullet, BBB2)
            BBB3 = Bbullet.Blue_Bullet2(self.x, self.y,  self.Number-1, 50 * math.sqrt(2), -50 * math.sqrt(2))
            gfw.world.add(gfw.layer.MonsterBullet, BBB3)
            BBB4 = Bbullet.Blue_Bullet2(self.x, self.y, self.Number-1, 0, -100)
            gfw.world.add(gfw.layer.MonsterBullet, BBB4)
            BBB5 = Bbullet.Blue_Bullet2(self.x, self.y,  self.Number-1, -50 * math.sqrt(2), -50 * math.sqrt(2))
            gfw.world.add(gfw.layer.MonsterBullet, BBB5)
            BBB6 = Bbullet.Blue_Bullet2(self.x, self.y,  self.Number-1, -100, 0)
            gfw.world.add(gfw.layer.MonsterBullet, BBB6)
            BBB7 = Bbullet.Blue_Bullet2(self.x, self.y,  self.Number-1, -50 * math.sqrt(2), 50 * math.sqrt(2))
            gfw.world.add(gfw.layer.MonsterBullet, BBB7)
            self.remove()

    def remove(self):
        gfw.world.remove(self)

    def draw(self):
        self.image.clip_draw(450 * int(self.frame), 0, 450, 450, self.x, self.y, 50, 50)

