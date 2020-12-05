from pico2d import *
import random
import math
import gfw

import BlueBullet
import Effect
import SoundM

class Blue_Bullet:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.radius = 25
        self.isDead = False
        self.frame = 0
        self.lifeTime = random.randint(100, 300) / 100
        self.deathTime = 0
        self.index = 0
        self.Sound = SoundM
        self.number = 0
        self.randomSpeed_Delta = random.randint(30, 50) / 100

        if Blue_Bullet.image is None:
            Blue_Bullet.image = load_image('res/Blue_Bullet2.png')
        for player in gfw.world.objects_at(gfw.layer.Player):
         self.deltaX = self.x - player.x
         self.deltaY = self.y - player.y

    def Bullet_LifeTime(self):
        self.deathTime += gfw.delta_time
        if self.deathTime > self.lifeTime:
            self.isDead = True

    def update(self):
        self.Bullet_LifeTime()
        self.x -= self.deltaX * gfw.delta_time * self.randomSpeed_Delta
        self.y -= self.deltaY * gfw.delta_time * self.randomSpeed_Delta
        self.frame += gfw.delta_time * 15

        if self.frame >= 15:
            self.frame = 0

        if self.isDead is True:
            Bf1 = Effect.Effect(self.x, self.y, 80, 80, 100, 100, 10, 7, 0.5)
            gfw.world.add(gfw.layer.Effect, Bf1)
            self.Sound.playSound(12, 40)
            BBB = BlueBullet.Blue_Bullet2(self.x, self.y, self.number - 1, 0, 100)
            gfw.world.add(gfw.layer.MonsterBullet, BBB)
            BBB1 = BlueBullet.Blue_Bullet2(self.x, self.y, self.number - 1, 50 * math.sqrt(2), 50 * math.sqrt(2))
            gfw.world.add(gfw.layer.MonsterBullet, BBB1)
            BBB2 = BlueBullet.Blue_Bullet2(self.x, self.y, self.number-1, 100, 0)
            gfw.world.add(gfw.layer.MonsterBullet, BBB2)
            BBB3 = BlueBullet.Blue_Bullet2(self.x, self.y, self.number-1, 50 * math.sqrt(2), -50 * math.sqrt(2))
            gfw.world.add(gfw.layer.MonsterBullet, BBB3)
            BBB4 = BlueBullet.Blue_Bullet2(self.x, self.y, self.number-1, 0, -100)
            gfw.world.add(gfw.layer.MonsterBullet, BBB4)
            BBB5 = BlueBullet.Blue_Bullet2(self.x, self.y, self.number-1, -50 * math.sqrt(2), -50 * math.sqrt(2))
            gfw.world.add(gfw.layer.MonsterBullet, BBB5)
            BBB6 = BlueBullet.Blue_Bullet2(self.x, self.y, self.number-1, -100, 0)
            gfw.world.add(gfw.layer.MonsterBullet, BBB6)
            BBB7 = BlueBullet.Blue_Bullet2(self.x, self.y, self.number-1, -50 * math.sqrt(2), 50 * math.sqrt(2))
            gfw.world.add(gfw.layer.MonsterBullet, BBB7)
            self.remove()

    def remove(self):
        gfw.world.remove(self)

    def draw(self):
        self.image.clip_draw(450 * int(self.frame), 0, 450, 450, self.x, self.y, 50, 50)
