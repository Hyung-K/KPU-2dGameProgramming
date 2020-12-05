from pico2d import *
import gfw
import random

import Item
import Effect
import MonsterBullet
import UI
import SoundM

checkDead = False

class BluePlane:
    image = None

    def __init__(self, x, y):
        self.hp = 50
        self.x, self.y = x, y
        self.radianX, self.pivotY = 40, 10
        self.FstX, self.FstY = x, y
        self.SndX, self.SndY = x + 200, y - 1000
        self.TrdX, self.TrdY = x + 400, y + 200
        self.frame = 0
        self.t = 0
        self.Sound = SoundM
        self.isDead = False
        self.initialize = False

        if BluePlane.image is None:
            BluePlane.image = load_image('res/Monster_1.png')

    def update(self):
        if self.isDead or self.hp <= 0:
            UI.Score().Add_Score(random.randint(70, 100))
            Eft3 = Effect.Effect(self.x + random.randint(-20, 20),
                                 self.y + random.randint(-20, 20),
                                 128, 128, 200, 200, 9, 1)
            gfw.world.add(gfw.layer.Effect, Eft3)
            self.Sound.playSound(2, 30)
            self.remove()

        if self.initialize is False and self.t > 0.5:
            self.initialize = True
            Bb = MonsterBullet.Monster1_Bullet(self.x, self.y, 0)
            gfw.world.add(gfw.layer.MonsterBullet, Bb)

        if self.t > 1:
            self.remove()

        self.frame = (self.frame + gfw.delta_time * 11) % 11
        self.t += gfw.delta_time * 0.3
        self.x = (1 - self.t) ** 2 * self.FstX + 2 * self.t * (1 - self.t) * self.SndX + self.t ** 2 * self.TrdX
        self.y = (1 - self.t) ** 2 * self.FstY + 2 * self.t * (1 - self.t) * self.SndY + self.t ** 2 * self.TrdY

    def draw(self):
        self.image.clip_draw(int(self.frame) * 32, 0, 32, 36, self.x, self.y, 80, 80)

    def remove(self):
        gfw.world.remove(self)


class RedPlane:
    image = None

    def __init__(self, x, y):
        self.hp = 50
        self.x, self.y = x, y
        self.radianX, self.pivotY = 40, 10
        self.isDead = False
        self.FstX, self.FstY = x, y
        self.SndX, self.SndY = x + 200, y - 1000
        self.TrdX, self.TrdY = x + 400, y + 200
        self.frame = 0
        self.t = 0
        self.Sound = SoundM
        self.initialize = False
        if RedPlane.image is None:
            RedPlane.image = load_image('res/Monster_2.png')

    def update(self):
        if self.isDead or self.hp <= 0:
            UI.Score().Add_Score(random.randint(200, 300))
            Eft4 = Effect.Effect(self.x + random.randint(-20, 20),
                                 self.y + random.randint(-20, 20),
                                 128, 128, 200, 200, 9, 1)
            gfw.world.add(gfw.layer.Effect, Eft4)
            RItem = Item.Item_Power(self.x, self.y)
            gfw.world.add(gfw.layer.Item, RItem)
            self.Sound.playSound(2, 30)
            self.remove()

        if self.initialize is False and self.t > 0.5:
            self.initialize = True
            RB = MonsterBullet.Monster1_Bullet(self.x, self.y, 0)
            gfw.world.add(gfw.layer.MonsterBullet, RB)

        if self.t > 1:
            self.remove()

        self.frame = (self.frame + gfw.delta_time * 11) % 11
        self.t += gfw.delta_time * 0.3
        self.x = (1 - self.t) ** 2 * self.FstX + 2 * self.t * (1 - self.t) * self.SndX + self.t ** 2 * self.TrdX
        self.y = (1 - self.t) ** 2 * self.FstY + 2 * self.t * (1 - self.t) * self.SndY + self.t ** 2 * self.TrdY

    def draw(self):
        self.image.clip_draw(int(self.frame) * 32, 0, 32, 36, self.x, self.y, 80, 80)

    def remove(self):
        gfw.world.remove(self)


class WhitePlane:
    image = None
    deltaX = 0
    deltaY = 0

    def __init__(self, x, y):
        self.hp = 50
        self.x, self.y = x, y
        self.radianX, self.pivotY = 40, 10
        self.isDead = False
        self.frame = 0
        self.t = 0
        self.Sound = SoundM

        for player in gfw.world.objects_at(gfw.layer.Player):
            self.DeltaX = player.x - x
            self.DeltaY = player.y - y

        if WhitePlane.image is None:
            WhitePlane.image = load_image('res/Monster_3.png')

    def update(self):
        if self.isDead or self.hp <= 0:
            UI.Score().Add_Score(random.randint(200, 300))
            Eft5 = Effect.Effect(self.x + random.randint(-20, 20),
                                 self.y + random.randint(-20, 20),
                                 128, 128, 200, 200, 9, 1)
            gfw.world.add(gfw.layer.Effect, Eft5)
            self.Sound.playSound(2, 30)
            self.remove()

        if self.t > 1:
            self.remove()
        self.frame = (self.frame + gfw.delta_time * 11) % 11
        self.x += self.deltaX * gfw.delta_time * 0.7
        self.y += self.deltaY * gfw.delta_time * 0.7

    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y, 80, 80)

    def remove(self):
        gfw.world.remove(self)


class BigPlane:
    image = None

    def __init__(self, x, y):
        self.hp = 15000
        self.x, self.y = x, y
        self.radianX, self.pivotY = 250, 20
        self.dist = 0
        self.bulletTerm = 0
        self.bigBulletTerm = 0
        self.bulletPossibleTime = 0
        self.bigBulletPossibleTime = 0
        self.Sound = SoundM
        self.isDead = False

        if BigPlane.image is None:
            BigPlane.image = load_image('res/BigAirPlane.png')

    def update(self):
        global checkDead
        if self.isDead or self.hp <= 0:
            UI.Score().Add_Score(random.randint(5000, 6000))
            Bf1 = Effect.Effect(self.x + random.randint(-20, 20),
                                self.y + random.randint(-20, 20),
                                252, 200, 600, 500, 14, 6, 0.5)
            gfw.world.add(gfw.layer.Effect, Bf1)
            Bitem = Item.Item_Bomb(self.x, self.y)
            gfw.world.add(gfw.layer.Item, Bitem)
            checkDead = True
            self.Sound.playSound(0, 50)
            self.remove()

        if self.y > 900:
            self.y -= 30 * gfw.delta_time
        self.bigBulletPossibleTime += gfw.delta_time * 1
        self.bulletPossibleTime += gfw.delta_time * 1

        if self.bigBulletPossibleTime > 3:
            self.bigBulletPossibleTime = 0
        if self.bigBulletPossibleTime > 1.5:
            self.bigBulletTerm += gfw.delta_time * 1
            if self.bigBulletTerm > 0.03:
                self.bigBulletTerm = 0
                SMB = MonsterBullet.PlaneBullet2(self.x, self.y - 150, 2,
                                                 random.randint(-360, 360), random.randint(500, 700))
                gfw.world.add(gfw.layer.MonsterBullet, SMB)

        if self.bulletPossibleTime > 1.5:
            self.bulletPossibleTime = 0
        if self.bulletPossibleTime > 1:
            self.bulletTerm += gfw.delta_time * 1
            if self.bulletTerm > 0.1:
                self.bulletTerm = 0
                CMB = MonsterBullet.Monster1_Bullet(self.x - 120, self.y - 50, 0)
                gfw.world.add(gfw.layer.MonsterBullet, CMB)
                CMB2 = MonsterBullet.Monster1_Bullet(self.x + 120, self.y - 50, 0)
                gfw.world.add(gfw.layer.MonsterBullet, CMB2)

    def draw(self):
        self.image.draw(self.x, self.y, 500, 400)

    def remove(self):
        gfw.world.remove(self)


class MidPlane:
    image = None

    def __init__(self, x, y, dir):
        self.hp = 2500
        self.x, self.y = x, y
        self.dir = dir
        self.frame = 0
        self.radianX, self.pivotY = 100, 20
        self.dist = 0
        self.bulletTerm = 0
        self.bulletPossibleTime = 0
        self.isDead = False
        if MidPlane.image is None:
            MidPlane.image = load_image('res/MidAirPlane.png')

    def initMove(self):
        if self.dir == -1 and self.x > 540:
            self.x -= gfw.delta_time * 100

        elif self.dir == 1 and self.x < 180:
            self.x += gfw.delta_time * 100

    def update(self):
        self.initMove()
        if self.isDead or self.hp <= 0:
            UI.Score().Add_Score(random.randint(1000, 1500))
            Mf = Effect.Effect(self.x + random.randint(-20, 20),
                               self.y + random.randint(-20, 20),
                               128, 128, 200, 200, 9, 1)
            gfw.world.add(gfw.layer.Effect, Mf)
            self.remove()

        if self.y > 800:
            self.y -= 70 * gfw.delta_time

        self.bulletPossibleTime += gfw.delta_time
        self.frame += gfw.delta_time * 5
        self.frame = self.frame % 2

        if self.bulletPossibleTime > 4:
            self.bulletPossibleTime = 0
        if self.bulletPossibleTime > 3:
            self.bulletTerm += gfw.delta_time * 1
            if self.bulletTerm > 0.1:
                self.bulletTerm = 0

                Mb = MonsterBullet.PlaneBullet3(self.x - 100, self.y - 50, -100, 0, 300)
                gfw.world.add(gfw.layer.MonsterBullet, Mb)
                Mb2 = MonsterBullet.PlaneBullet3(self.x, self.y - 50, 0, 0, 400)
                gfw.world.add(gfw.layer.MonsterBullet, Mb2)
                Mb3 = MonsterBullet.PlaneBullet3(self.x + 100, self.y - 50, 100, 0, 300)
                gfw.world.add(gfw.layer.MonsterBullet, Mb3)

    def draw(self):
        self.image.clip_draw(int(self.frame) * 310, 0, 310, 335, self.x, self.y, 200, 200)

    def remove(self):
        gfw.world.remove(self)