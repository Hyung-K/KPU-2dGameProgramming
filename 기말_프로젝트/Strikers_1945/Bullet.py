from pico2d import *
from gobj import *
import gfw

import Effect

name = 'Bullet'


class Bullet():
    image = [None, None, None, None]

    def __init__(self, x, y, speed=720):
        self.x, self.y = x, y
        self.dy = speed
        self.isDead = False

        if self.image[0] == None:
            self.image[0] = load_image('res/Bullet_Eg_a.png')

        if self.image[1] == None:
            self.image[1] = load_image('res/Bullet_Eg_b.png')

        if self.image[2] == None:
            self.image[2] = load_image('res/Bullet_Eg_c.png')

        if self.image[3] == None:
            self.image[3] = load_image('res/Bullet_Eg_d.png')

    def update(self):
        self.y += self.dy * gfw.delta_time
        if self.isDead == True or self.y > get_canvas_height() + 20:
            self.remove()

    def draw(self):
        for player in gfw.world.objects_at(gfw.layer.Player):
            self.image[player.power].draw(self.x - 7, self.y + 10, 120, 120)

    def remove(self):
        gfw.world.remove(self)


class Player_Laser():
    image = None

    def __init__(self, x):
        self.deltaX = x
        self.isDead = False
        self.frame = 0
        self.lifeTime = 0

        for player in gfw.world.objects_at(gfw.layer.Player):
            self.x, self.y = player.x + self.deltaX, player.y
        if Player_Laser.image == None:
            Player_Laser.image = load_image('res/fire_lazer.png')

    def update(self):
        self.lifeTime += 1
        for player in gfw.world.objects_at(gfw.layer.Player):
            self.x = player.x + self.deltaX
            self.y = player.y

        for Monster in gfw.world.objects_at(gfw.layer.Monster):
            if Monster.x - Monster.radianX < self.x < Monster.x + Monster.radianX and self.y < Monster.y:
                Pp = Effect.Effect(Monster.x + random.randint(-15, 15), 30, 27, 30, 27, 12, 0)
                gfw.world.add(gfw.layer.Effect, Pp)
                Monster.hp -= gfw.delta_time * 30
        self.lifeTime += 0.1
        self.frame = (self.frame + 1) % 80

        for player in gfw.world.objects_at(gfw.layer.Player):
            player.Gage -= 5 * gfw.delta_time

        if self.isDead is True or player.Gage <= 0:
            for player in gfw.world.objects_at(gfw.layer.Player):
                player.Gage = 0
                self.remove()

    def draw(self):
        self.image.clip_draw((self.frame // 10) * 60, 0, 80, 100, self.x, self.y + 480, 10, 960)

    def remove(self):
        gfw.world.remove(self)