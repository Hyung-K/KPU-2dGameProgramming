from pico2d import *
import gfw
import random
import math

import Effect
import Bullet
import MonsterBullet
import HyperionBullet


class Hyperion:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        self.dist = 0
        self.t = 0
        self.dir = random.randint(0, 1)
        self.deltaY = 0
        self.bulletTerm = 0

        if Hyperion.image == None:
            Hyperion.image = load_image('res/Monster_4.png')

    def update(self):
        self.bulletTerm = (self.bulletTerm+gfw.delta_time*1)
        if self.bulletTerm >= 0.15:
            self.bulletTerm = 0
            Hbullet = HyperionBullet.Hyperion_Bullet(self.x, self.y + 20, 0)
            gfw.world.add(gfw.layer.Bullet, Hbullet)
            Hbullet2 = HyperionBullet.Hyperion_Bullet(self.x + 100, self.y, 1)
            gfw.world.add(gfw.layer.Bullet, Hbullet2)
            Hbullet3 = HyperionBullet.Hyperion_Bullet(self.x - 100, self.y, 2)
            gfw.world.add(gfw.layer.Bullet, Hbullet3)

        for Mb in gfw.world.objects_at(gfw.layer.MonsterBullet):
            if (self.x - 120 < Mb.x < self.x + 120) and  (self.y - 60 < Mb.y < self.y + 60):
                Mb.isDead = True
                if Mb.index == 2:
                    HE = Effect.Effect(Mb.x, Mb.y, 128, 128, 60, 60, 8, 4)
                    gfw.world.add(gfw.layer.Effect, HE)

        if self.deltaY < 300:
            self.y += gfw.delta_time * 100
            self.deltaY += gfw.delta_time * 100

        elif self.deltaY >= 300 and self.deltaY < 500:
            self.deltaY += gfw.delta_time * 50
            if self.dir == 0:
                self.y += gfw.delta_time * 50
                self.x -= gfw.delta_time * 50
            elif self.dir == 1:
                self.y += gfw.delta_time * 50
                self.x += gfw.delta_time * 50

        elif self.deltaY >= 500:
            if self.dir == 0:
                self.y += gfw.delta_time * 300
                self.x -= gfw.delta_time * 150
            elif self.dir == 1:
                self.y += gfw.delta_time * 300
                self.x += gfw.delta_time * 150

        if self.x < -60 or self.x > 780:
            self.remove()

    def draw(self):
        self.image.clip_draw(self.frame*240, 0, 240, 120, self.x, self.y,240,120)

    def remove(self):
        gfw.world.remove(self)

