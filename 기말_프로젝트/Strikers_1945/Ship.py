from pico2d import *

import gfw
import random
import Effect
import Bullet
import MonsterBullet
import Posin
import UI

class BossShip:
    image1 = None
    image2 = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        self.dist = 0
        self.deathCnt = 0
        self.effectTerm = 0
        self.deathSizeX = 0
        self.deathSizeY = 0
        self.moveSpeed = 100

        self.isDead = False
        self.bisOpen = False
        self.lInit = False

        if BossShip.image1 == None:
            BossShip.image1 = load_image('res/Ship.png')
        if BossShip.image2 == None:
            BossShip.image2 = load_image('res/Ship2.png')
        self.bigPosin1 = Posin.bigPosin(self.x-360, self.y)
        gfw.world.add(gfw.layer.Monster, self.bigPosin1)
        self.bigPosin2 = Posin.bigPosin(self.x-248, self.y)
        gfw.world.add(gfw.layer.Monster, self.bigPosin2)
        self.bigPosin3 = Posin.bigPosin(self.x + 336, self.y)
        gfw.world.add(gfw.layer.Monster, self.bigPosin3)
        self.bigPosinLst = [self.bigPosin1, self.bigPosin2, self.bigPosin3]

        self.midPosin1 = Posin.midPosin(self.x - 72.5, self.y-20)
        gfw.world.add(gfw.layer.Monster, self.midPosin1)
        self.midPosin2 = Posin.midPosin(self.x - 72.5, self.y + 54)
        gfw.world.add(gfw.layer.Monster, self.midPosin2)
        self.midPosin3 = Posin.midPosin(self.x + 167.5, self.y - 20)
        gfw.world.add(gfw.layer.Monster, self.midPosin3)
        self.midPosin4 = Posin.midPosin(self.x + 167.5, self.y + 54)
        gfw.world.add(gfw.layer.Monster, self.midPosin4)
        self.midPosinLst = [self.midPosin1, self.midPosin2, self.midPosin3, self.midPosin4]

        self.smlPosin1 = Posin.smlPosin(self.x + 20, self.y + 84)
        gfw.world.add(gfw.layer.Monster, self.smlPosin1)
        self.smlPosin2 = Posin.smlPosin(self.x + 20, self.y - 62)
        gfw.world.add(gfw.layer.Monster, self.smlPosin2)
        self.smlPosin3 = Posin.smlPosin(self.x + 75.5, self.y + 84)
        gfw.world.add(gfw.layer.Monster, self.smlPosin3)
        self.smlPosin4 = Posin.smlPosin(self.x + 75.5, self.y - 62)
        gfw.world.add(gfw.layer.Monster, self.smlPosin4)
        self.smlPosin5 = Posin.smlPosin(self.x - 200, self.y + 74)
        gfw.world.add(gfw.layer.Monster, self.smlPosin5)
        self.smlPosin6 = Posin.smlPosin(self.x - 200, self.y - 52)
        gfw.world.add(gfw.layer.Monster, self.smlPosin6)
        self.smlPosinLst = [self.smlPosin1, self.smlPosin2, self.smlPosin3, self.smlPosin4, self.smlPosin5, self.smlPosin6]

    def initMove(self):
        if self.x > 390:
            for Posin in self.bigPosinLst:
                Posin.x -= gfw.delta_time * self.moveSpeed
            for Posin in self.midPosinLst:
                Posin.x -= gfw.delta_time * self.moveSpeed
            for Posin in self.smlPosinLst:
                Posin.x -= gfw.delta_time * self.moveSpeed
            self.x -= gfw.delta_time * self.moveSpeed

        else:
            if self.bisOpen is False:
                self.bisOpen = True
                for bigPosin in self.bigPosinLst:
                    bigPosin.bisOpen = True

    def bossDead(self):
        if self.deathCnt >= 13:
            self.deathSizeX += gfw.delta_time * (137.5/2)
            self.deathSizeY += (gfw.delta_time * 10)
            self.effectTerm += gfw.delta_time
            if self.effectTerm > 0.1 and self.deathSizeX < 600:
                self.effectTerm = 0
                DEf = Effect.Effect(self.x + random.randint(int(-700 + self.deathSizeX), int(700-self.deathSizeX)),
                                    self.y + random.randint(int(-100 + self.deathSizeY), int(100-self.deathSizeY)),
                                    149, 149, 250, 250, 32, 8, 0.3)
                gfw.world.add(gfw.layer.Effect, DEf)

        if self.lInit is False and self.deathSizeX > 600:
            self.lInit = True
            UI.FinalScore()

    def update(self):
        self.bossDead()
        self.initMove()
        if self.isDead:
            BcEf = Effect.Effect(self.x + random.randint(-20, 20),
                                 self.y + random.randint(-20, 20),
                                 128, 128, 200, 200, 9, 1)
            gfw.world.add(gfw.layer.Effect, BcEf)
            self.remove()

    def draw(self):
        if self.deathCnt < 13:
            self.image1.draw(self.x, self.y, 1375, 200)
        else:
            self.image2.draw(self.x, self.y, 1375 - self.deathSizeX, 200 - self.deathSizeY)

    def remove(self):
        gfw.world.remove(self)
