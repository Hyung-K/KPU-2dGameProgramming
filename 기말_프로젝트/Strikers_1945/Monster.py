from pico2d import *
import gfw
import random

import MonsterBullet
import Effect
import UI
import SoundM

class LeftPlane1():
    image = None

    def __init__(self, x, y):
        self.hp = 20
        self.x, self.y = x, y
        self.radianX, self.pivotY = 40, 10
        self.frame = 0
        self.bulletTerm = 0
        self.dist = 0
        self.Sound = SoundM
        self.isDead = False
        if LeftPlane1.image is None:
            LeftPlane1.image = load_image('res/Monster_6_left.png')

    def update(self):
        if self.isDead or self.hp <= 0:
             UI.Score().Add_Score(random.randint(100, 150))
             Ef1 = Effect.Effect(self.x + random.randint(-20, 20), self.y + random.randint(-20, 20), 128, 128, 200, 200, 9, 1)
             gfw.world.add(gfw.layer.Effect, Ef1)
             self.Sound.playSound(1, 30)
             self.remove()
        self.bulletTerm = (self.bulletTerm + gfw.delta_time * 3) % 3
        if self.bulletTerm > 2.5:
            self.bulletTerm = 0
            Lb = MonsterBullet.PlaneBullet(self.x, self.y, 0)
            gfw.world.add(gfw.layer.MonsterBullet, Lb)

        if self.y < 750:
            self.x -= 100 * gfw.delta_time
            self.frame = 1
            if self.x < -30:
                self.remove()
        self.y -= 100 * gfw.delta_time

    def draw(self):
        self.image.clip_draw(self.frame * 42, 0, 42, 34, self.x, self.y, 80, 80)

    def remove(self):
        gfw.world.remove(self)

class RightPlane1():
    image = None

    def __init__(self, x, y):
        self.hp = 50
        self.x, self.y = x, y
        self.radianX, self.pivotY = 40, 10
        self.frame = 0
        self.dist = 0
        self.Sound = SoundM
        self.isDead = False
        self.bulletTerm = 0

        if RightPlane1.image == None:
            RightPlane1.image = load_image('res/Monster_6_right.png')

    def update(self):
        if self.isDead or self.hp <= 0:
             UI.Score().Add_Score(random.randint(100, 150))
             Ef2 = Effect.Effect(self.x + random.randint(-20, 20), self.y + random.randint(-20, 20), 128, 128, 200, 200, 9, 1)
             gfw.world.add(gfw.layer.Effect, Ef2)
             self.Sound.playSound(1, 40)
             self.remove()

        self.bulletTerm = (self.bulletTerm + gfw.delta_time * 3) % 3
        if self.bulletTerm > 2.5:
            self.bulletTerm = 0
            Rb = MonsterBullet.PlaneBullet(self.x, self.y, 0)
            gfw.world.add(gfw.layer.MonsterBullet, Rb)

        if self.y < 750:
            self.x += 100 * gfw.delta_time
            self.frame = 1
            if self.x < -30:
                self.remove()
        self.y -= 100 * gfw.delta_time

    def draw(self):
        self.image.clip_draw(self.frame * 42, 0, 42, 34, self.x, self.y, 80, 80)

    def remove(self):
        gfw.world.remove(self)


