from gobj import *

import gfw
import win32api
import Bullet
import Hyperion
import SoundM

class Player():
    PType = 0

    def __init__(self):
        self.x, self.y = 0, 90
        self.image = load_image('res/Player_T.png')
        self.image2 = load_image('res/Player_T2.png')
        self.image3 = load_image('res/Player_T3.png')
        self.image4 = load_image('res/Player_T4.png')
        self.image5 = load_image('res/Player_T5.png')
        self.frame = 3  # speed
        self.time = 0
        self.interval = 0
        self.playerState = 0
        self.life = 5
        self.preLife = self.life
        self.Gage = 0
        self.laserTime = 0
        self.power = 0  # 플레이어 파워
        self.bombNo = 2  # 필살기개수
        self.isShield = False
        self.shieldTime = 0
        self.SMode = False
        self.Sound = SoundM

    def Player_LifeSystem(self):
        if win32api.GetAsyncKeyState(0x44) & 0x1001:
            if self.SMode is True:
                self.SMode = False
            elif self.SMode is False:
                self.SMode = True

            if self.preLife != self.life:
                self.isShield = True
            self.preLife = self.life

        if self.isShield is True:
            self.shieldTime += gfw.delta_time
            if self.shieldTime > 3:
                self.shieldTime = 0
                self.isShield = False

    def fire(self):
        if win32api.GetAsyncKeyState(0x20) & 0x8000 and self.interval >= 1:  # space
            self.interval = 0
            bullet = Bullet.Bullet(self.x, self.y + 20)
            gfw.world.add(gfw.layer.Bullet, bullet)

    def Make_Hyperion(self):
        if win32api.GetAsyncKeyState(0x53) & 0x1001 and self.bombNo >= 1:  # s:
            self.bombNo -= 1
            Ch = Hyperion.Hyperion(360, 0)
            gfw.world.add(gfw.layer.Hyperion, Ch)
            Lh = Hyperion.Hyperion(200, -100)
            gfw.world.add(gfw.layer.Hyperion, Lh)
            Rh = Hyperion.Hyperion(520, -100)
            gfw.world.add(gfw.layer.Hyperion, Rh)

    def Make_Laser(self):
        if gfw.world.count_at(gfw.layer.Laser) > 0:
            self.laserTime += gfw.delta_time * 2
        if win32api.GetAsyncKeyState(0x41) & 0x1001:
            if gfw.world.count_at(gfw.layer.Laser) == 0 and self.Gage > 20:
                LayL = Bullet.Player_Laser(13)
                gfw.world.add(gfw.layer.Laser, LayL)
                LayR = Bullet.Player_Laser(-25)
                gfw.world.add(gfw.layer.Laser, LayR)

            elif self.laserTime > 3 and gfw.world.count_at(gfw.layer.Laser) > 0:
                self.laserTime = 0
                for Laser in gfw.world.objects_at(gfw.layer.Laser):
                    Laser.isDead = True

    def update(self):
        self.Player_LifeSystem()
        self.Make_Laser()
        self.Make_Hyperion()
        self.fire()
        self.interval += (20 * gfw.delta_time)
        self.x = clamp(40, self.x, 720)
        self.Gage = clamp(0, self.Gage, 100)
        self.y = clamp(40, self.y, 960)
        if (win32api.GetAsyncKeyState(0x25) & 0x8000 or
                win32api.GetAsyncKeyState(0x26) & 0x8000 or
                win32api.GetAsyncKeyState(0x27) & 0x8000 or
                win32api.GetAsyncKeyState(0x28) & 0x8000):
            if win32api.GetAsyncKeyState(0x25) & 0x8000:
                self.x -= 400 * gfw.delta_time
            if win32api.GetAsyncKeyState(0x27) & 0x8000:
                self.x += 400 * gfw.delta_time
            if win32api.GetAsyncKeyState(0x26) & 0x8000:
                self.y += 400 * gfw.delta_time
            if win32api.GetAsyncKeyState(0x28) & 0x8000:
                self.y -= 400 * gfw.delta_time
        else:
            playerState = 0

        self.time = (self.time + 1) % 50
        if win32api.GetAsyncKeyState(0x25) & 0x8000 and self.time >= 48:
            self.frame -= 1
        if win32api.GetAsyncKeyState(0x27) & 0x8000 and self.time >= 48:
            self.frame += 1

        if self.frame <= 0:
            self.frame = 0
        if self.frame >= 6:
            self.frame = 6

    def draw(self):
        if Player.PType == 1:
            self.image5.clip_draw(3 * 33, 0, 33, 33, self.x, self.y, 80, 80)
        elif Player.PType == 2:
            self.image3.clip_draw(3 * 33, 0, 33, 33, self.x, self.y, 80, 80)
        elif Player.PType == 3:
            self.image4.clip_draw(3 * 33, 0, 33, 33, self.x, self.y, 80, 80)
        elif Player.PType == 4:
            self.image.clip_draw(3 * 33, 0, 33, 33, self.x, self.y, 80, 80)
        elif Player.PType == 5:
            self.image2.clip_draw(3 * 33, 0, 33, 33, self.x, self.y, 80, 80)
