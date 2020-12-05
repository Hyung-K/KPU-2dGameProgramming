from pico2d import *
import gfw
import random
import math

import MonsterBullet
import BossBlueBullet
import Effect
import SoundM

class BigPosin:
    image = None

    def __init__(self, x, y):
        self.hp = 3000
        self.x, self.y = x, y
        self.frame = 0
        self.dist = 0
        self.isDead = False
        self.radianX, self.pivotY = 50, 50
        self.bisOpen = False
        self.bulletMakeTerm = 0
        self.Sound = SoundM
        self.randomDelta = random.randint(40, 90) / 100

        if BigPosin.image == None:
            BigPosin.image = load_image('res/BigPosin.png')

    def frame_Manegement(self):
        if self.bisOpen is True:
            self.frame += 10 * gfw.delta_time
            if self.frame > 32:
                self.frame = 24

    def Make_Bullet(self):
        self.bulletMakeTerm += gfw.delta_time * self.randomDelta
        if self.bulletMakeTerm > 5:
            self.randomDelta = random.randint(60, 90) / 100
            self.bulletMakeTerm = 0
            BM = BossBlueBullet.Blue_Bullet(self.x, self.y)
            gfw.world.add(gfw.layer.MonsterBullet, BM)

    def update(self):
        self.frame_Manegement()
        self.Make_Bullet()
        if self.isDead or self.hp < 0:
            PEf = Effect.Effect(self.x + random.randint(-20, 20), self.y + random.randint(-20, 20), 128, 128, 200, 200,
                                9, 1)
            gfw.world.add(gfw.layer.Effect, PEf)
            self.Sound.playSound(random.randint(3, 7), 40)

            for boss in gfw.world.objects_at(gfw.layer.Boss):
                boss.deathCnt += 1
                self.remove()

    def draw(self):
        self.image.clip_draw(int(self.frame) * 60, 0, 60, 60, self.x, self.y, 100, 100)

    def remove(self):
        gfw.world.remove(self)


class MidPosin:
    image = None

    def __init__(self, x, y):
        self.hp = 2000
        self.x, self.y = x, y
        self.frame = 0
        self.dist = 0
        self.isDead = False
        self.radianX, self.pivotY = 25, 25
        self.time = 0
        self.bulletTime = 3
        self.bulletPossibleTime = 0
        self.makeBulletTerm = 0
        self.Sound = SoundM
        self.bisBulletPossible = False

        if MidPosin.image is None:
            MidPosin.image = load_image('res/Boat_Posin.png')

    def makeBullet(self):
        self.time += gfw.delta_time
        if self.time > self.bulletTime and self.bisBulletPossible is False:
            self.bulletPossibleTime = random.randint(2, 4)
            self.bisBulletPossible = True
            self.time = 0
        if self.bisBulletPossible is True:
            self.makeBulletTerm += gfw.delta_time
            if self.makeBulletTerm > 0.5:
                self.makeBulletTerm = 0
                speed = random.randint(40, 70) / 100
                MbB1 = MonsterBullet.Monster1_Bullet(self.x - 7, self.y, 0, speed)
                gfw.world.add(gfw.layer.MonsterBullet, MbB1)
                MbB2 = MonsterBullet.Monster1_Bullet(self.x + 7, self.y, 0, speed)
                gfw.world.add(gfw.layer.MonsterBullet, MbB2)
                if self.bulletPossibleTime < self.time:
                    self.time = 0
                    self.bisBulletPossible = False
                    self.bulletTime = random.randint(2, 4)

    def dir_Calculate(self):
        for player in gfw.world.objects_at(gfw.layer.Player):
            X = player.x - self.x
            Y = self.y - player.y
        Cter = math.atan2(X, -Y)
        NCter = Cter * (180 / 3.14)

        if NCter < 0:
            NCter = 180 + (180 + NCter)
        self.Frame = NCter / 11.25

    def update(self):
        self.makeBullet()
        self.dir_Calculate()
        if self.isDead or self.hp < 0:
            PEf2 = Effect.Effect(self.x + random.randint(-20, 20), self.y + random.randint(-20, 20), 128, 128, 200, 200,
                                 9, 1)
            gfw.world.add(gfw.layer.Effect, PEf2)
            self.Sound.playSound(random.randint(3, 7), 40)

            for boss in gfw.world.objects_at(gfw.layer.Boss):
                boss.deathCnt += 1
            self.remove()

    def draw(self):
        self.image.clip_draw(int(self.frame) * 30, 0, 30, 30, self.x, self.y, 50, 50)

    def remove(self):
        gfw.world.remove(self)


class SmlPosin:
    image = None

    def __init__(self, x, y):
        self.hp = 1000
        self.x, self.y = x, y
        self.frame = 0
        self.dist = 0
        self.isDead = False
        self.radianX, self.pivotY = 30, 20
        self.bulletTime = 0
        self.Sound = SoundM
        self.makeBulletTerm = random.randint(20, 40) / 10
        if SmlPosin.image is None:
            SmlPosin.image = load_image('res/Boat_Posin2.png')

    def dir_Calculate(self):
        for player in gfw.world.objects_at(gfw.layer.Player):
            X = player.x - self.x
            Y = self.y - player.y
        Cter = math.atan2(X, -Y)
        NCter = Cter * (180 / 3.14)
        if NCter < 0:
            NCter = 180 + (180 + NCter)
        self.frame = NCter / 11.25

    def makeBullet(self):
        self.bulletTime += gfw.delta_time
        if self.makeBulletTerm < self.bulletTime:
            self.bulletTime = 0
            self.makeBulletTerm = random.randint(20, 40) / 10
            speed = random.randint(70, 100) / 100
            SpB = MonsterBullet.Monster1_Bullet(self.x, self.y, 0, speed)
            gfw.world.add(gfw.layer.MonsterBullet, SpB)

    def update(self):
        self.makeBullet()
        self.dir_Calculate()

        if self.isDead or self.hp < 0:
            ScE = Effect.Effect(self.x + random.randint(-20, 20), self.y + random.randint(-20, 20),
                                128, 128, 200, 200, 9, 1)
            gfw.world.add(gfw.layer.MonsterBullet, ScE)
            self.Sound.playSound(random.randint(3, 7), 40)

            for boss in gfw.world.objects_at(gfw.layer.Boss):
                boss.deathCnt += 1
            self.remove()

    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 0, 40, 30, self.x, self.y, 60, 40)

    def remove(self):
        gfw.world.remove(self)
