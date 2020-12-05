from pico2d import *
import gfw
import random

import Effect
import Posin
import UI
import SoundM

class BossShip:
    image1 = None
    image2 = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        self.dist = 0
        self.isDead = False
        self.deathCnt = 0
        self.effectTerm = 0
        self.deathSizeX = 0
        self.deathSizeY = 0
        self.Sound = SoundM
        self.bisOpen = False
        self.LInit = False
        self.MoveSpeed = 100

        if BossShip.image1 == None:
            BossShip.image1 = load_image('res/Ship.png')
        if BossShip.image2 == None:
            BossShip.image2 = load_image('res/Ship2.png')

        self.SmlPosin1 = Posin.SmlPosin(self.x + 20, self.y + 84)
        gfw.world.add(gfw.layer.Monster, self.SmlPosin1)
        self.SmlPosin2 = Posin.SmlPosin(self.x + 20, self.y - 62)
        gfw.world.add(gfw.layer.Monster, self.SmlPosin2)
        self.SmlPosin3 = Posin.SmlPosin(self.x + 75.5, self.y + 84)
        gfw.world.add(gfw.layer.Monster, self.SmlPosin3)
        self.SmlPosin4 = Posin.SmlPosin(self.x + 75.5, self.y - 62)
        gfw.world.add(gfw.layer.Monster, self.SmlPosin4)
        self.SmlPosin5 = Posin.SmlPosin(self.x - 200, self.y + 74)
        gfw.world.add(gfw.layer.Monster, self.SmlPosin5)
        self.SmlPosin6 = Posin.SmlPosin(self.x - 200, self.y - 52)
        gfw.world.add(gfw.layer.Monster, self.SmlPosin6)
        self.SmlPosinLst = [self.SmlPosin1, self.SmlPosin2, self.SmlPosin3, self.SmlPosin4, self.SmlPosin5, self.SmlPosin6]

        self.MidPosin1 = Posin.MidPosin(self.x - 72.5, self.y - 20)
        gfw.world.add(gfw.layer.Monster, self.MidPosin1)
        self.MidPosin2 = Posin.MidPosin(self.x - 72.5, self.y + 54)
        gfw.world.add(gfw.layer.Monster, self.MidPosin2)
        self.MidPosin3 = Posin.MidPosin(self.x + 167.5, self.y - 20)
        gfw.world.add(gfw.layer.Monster, self.MidPosin3)
        self.MidPosin4 = Posin.MidPosin(self.x + 167.5, self.y + 54)
        gfw.world.add(gfw.layer.Monster, self.MidPosin4)
        self.MidPosinLst = [self.MidPosin1, self.MidPosin2, self.MidPosin3, self.MidPosin4]

        self.BigPosin1 = Posin.BigPosin(self.x-360, self.y)
        gfw.world.add(gfw.layer.Monster,self.BigPosin1)
        self.BigPosin2 = Posin.BigPosin(self.x-248, self.y)
        gfw.world.add(gfw.layer.Monster,self.BigPosin2)
        self.BigPosin3 = Posin.BigPosin(self.x + 336, self.y)
        gfw.world.add(gfw.layer.Monster,self.BigPosin3)
        self.BigPosinLst = [self.BigPosin1, self.BigPosin2, self.BigPosin3]

    def bossDead(self):
        if self.deathCnt >= 13:
            self.deathSizeX += gfw.delta_time * (137.5 / 2)
            self.deathSizeY += (gfw.delta_time * 10)
            self.effectTerm += gfw.delta_time

            if self.effectTerm > 0.1 and self.deathSizeX < 600:
                self.Sound.playSound(random.randint(3, 7), 50)
                self.effectTerm = 0
                DEf = Effect.Effect(self.x + random.randint(int(-700 + self.deathSizeX), int(700 - self.deathSizeX)),
                                    self.y + random.randint(int(-100 + self.deathSizeY), int(100 - self.deathSizeY)),
                                    149, 149, 250, 250, 32, 8, 0.3)
                gfw.world.add(gfw.layer.Effect, DEf)

        if self.LInit is False and self.deathSizeX > 600:
            self.LInit = True
            UI.FinalScore()

    def initMove(self):
        if self.x > 390:
            for Posin in self.SmlPosinLst:
                Posin.x -= gfw.delta_time * self.MoveSpeed
            for Posin in self.MidPosinLst:
                Posin.x -= gfw.delta_time * self.MoveSpeed
            for Posin in self.BigPosinLst:
                Posin.x -= gfw.delta_time * self.MoveSpeed
            self.x -= gfw.delta_time * self.MoveSpeed
          
        else:
            if self.bisOpen is False:
                self.bisOpen = True
                for BigPosin in self.BigPosinLst:
                   BigPosin.bisOpen = True


    def update(self):
        self.bossDead()
        self.initMove()
        if self.isDead:
            BcEf = Effect.Effect(self.x + random.randint(-20, 20),
                                 self.y + random.randint(-20, 20),128, 128, 200, 200, 9, 1)
            gfw.world.add(gfw.layer.Effect, BcEf)
            self.remove()

    def draw(self):
        if self.deathCnt < 13:
            self.image1.draw(self.x, self.y, 1375, 200)
        else:
            self.image2.draw(self.x, self.y, 1375 - self.deathSizeX, 200 - self.deathSizeY)

    def remove(self):
        gfw.world.remove(self)