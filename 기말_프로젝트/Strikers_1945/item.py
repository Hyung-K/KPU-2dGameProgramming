from pico2d import *
import gfw
import math

import Monster2
import Effect
import SoundM
import Player

class Item_Bomb():
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        self.state1 = 'L'
        self.state2 = 'T'
        self.Sound = SoundM

        if Item_Bomb.image == None:
            Item_Bomb.image = load_image('res/Item_Bomb.png')

    def Item_Move(self):
        if self.state1 == 'L':
            self.x -= gfw.delta_time * 200
            if self.x <= 0:
                self.state1 = 'R'
        elif self.state1 == 'R':
            self.x += gfw.delta_time * 200
            if self.x >= 720:
                self.state1 = 'L'

        if self.state2 == 'T':
            self.y += gfw.delta_time * 400
            if self.y >= 960:
                self.state2 = 'B'
        elif self.state2 == 'B':
            self.y -= gfw.delta_time * 400
            if self.y <= 0:
                self.state2 = 'T'

    def update(self):
        for Player in gfw.world.objects_at(gfw.layer.Player):
            distance = math.sqrt((Player.x - self.x) ** 2 + (Player.y - self.y) ** 2)
            if distance < 30:
                Pp = Effect.Effect(self.x, self.y, 144, 100, 80, 50, 8, 2)
                gfw.world.add(gfw.layer.Effect, Pp)
                self.Sound.playSound(10, 30)

                if Player.bombNo < 4:
                    Player.bombNo += 1
                self.remove()
        self.Item_Move()
        self.frame = (self.frame + gfw.delta_time * 6) % 4

    def draw(self):
        self.image.clip_draw(int(self.frame) * 54, 0, 54, 32, self.x, self.y, 50, 30)

    def remove(self):
        gfw.world.remove(self)

class Item_Power():
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.frame = 0
        self.state1 = 'L'
        self.state2 = 'T'
        self.Sound = SoundM

        if Item_Power.image == None:
            Item_Bomb.image = load_image('res/Item_Power.png')

        self.PlayerX = 0  # player.x
        self.PlayerY = 0  # player.y
        self.PlayerPower = 0  # player.Power

    def Item_Move(self):
        if self.state1 == 'L':
            self.x -= gfw.delta_time * 200
            if self.x <= 0:
                self.state1 = 'R'

        elif self.state1 == 'R':
            self.x += gfw.delta_time * 200
            if self.x >= 720:
                self.state1 = 'L'

        if self.state2 == 'T':
            self.y += gfw.delta_time * 400
            if self.y >= 960:
                self.state2 = 'B'

        elif self.state2 == 'B':
            self.y -= gfw.delta_time * 400
            if self.y <= 0:
                self.state2 = 'T'

    def update(self):
        for player in gfw.world.objects_at(gfw.layer.Player):
            self.PlayerX = player.x
            self.PlayerY = player.y
            self.PlayerPower = player.power
        distance = math.sqrt((self.PlayerX - self.x) ** 2 + (self.PlayerY - self.y) ** 2)

        if distance < 30:
            self.Sound.playSound(10, 30)
            if self.PlayerPower < 3:
                for player in gfw.world.objects_at(gfw.layer.Player):
                    player.power += 1
                    pp = Effect.Effect(self.x, self.y, 144, 100, 80, 50, 8, 2)
                    gfw.world.add(gfw.layer.Effect, pp)
            self.remove()

        self.Item_Move()
        self.frame = (self.frame + gfw.delta_time*9) % 6

    def draw(self):
        self.image.clip_draw(int(self.frame) * 25, 0, 25, 18, self.x, self.y, 50, 30)
        pass

    def remove(self):
        gfw.world.remove(self)
