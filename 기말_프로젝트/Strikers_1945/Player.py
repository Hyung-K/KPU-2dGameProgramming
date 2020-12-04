from pico2d import *
import gfw
from gobj import *
import win32api
import Bullet 
import hyperion

class Player():
    def __init__(self):
        self.x, self.y = 0, 90
        self.image = load_image('res/Player_T.png')
        self.Frame = 3    # speed
        self.Time = 0
        self.Interval = 0
        self.PlayerState = 0

        self.Life = 5
        self.BombNo = 2     # 필살기
        self.Gage = 0
        self.Power = 0
        self.LagerTime = 0
        self.SoundDelta = 0
        self.isShield = False
        self.ShieldTime = 0

        self.SMode = False

    def Make_Hyperion(self):
        if win32api.GetAsyncKeyState(0x53) & 0x1001 and self.BombNo >= 1:  # s:
            self.BombNo -= 1
            Ch = hyperion.Hyperion(360, 0)
            gfw.world.add(gfw.layer.Hyperion, Ch)
            Lh = hyperion.Hyperion(200, -100)
            gfw.world.add(gfw.layer.Hyperion, Lh)
            Rh = hyperion.Hyperion(520, -100)
            gfw.world.add(gfw.layer.Hyperion, Rh)

    def Make_Lager(self):
        if gfw.world.count_at(gfw.layer.CLazer) > 0:
            self.LagerTime += gfw.delta_time
        if win32api.GetAsyncKeyState(0x41) & 0x1001:
            if gfw.world.count_at(gfw.layer.CLazer) == 0 and self.Gage > 20:  # a
                LayL = Bullet.Player_Lager(25)
                gfw.world.add(gfw.layer.Lazer, LayL)
                LayR = Bullet.Player_Lager(-25)
                gfw.world.add(gfw.layer.Lazer, LayR)

            elif self.LagerTime > 3 and gfw.world.count_at(gfw.layer.CLazer) > 0:
                self.LagerTime = 0
                for Lager in gfw.world.objects_at(gfw.layer.CLazer):
                    Lager.isDead = True

    def fire(self):
        if win32api.GetAsyncKeyState(0x20) & 0x8000 and self.Interval >= 1:  # space
            self.Interval = 0
            bullet = Bullet.Bullet(self.x, self.y + 20)
            gfw.world.add(gfw.layer.Bullet, bullet)

    def update(self):
        self.fire()
        self.Interval += (20 * gfw.delta_time)
        self.x = clamp(40, self.x, 700)
        self.Gage = clamp(0, self.Gage, 100)
        self.y = clamp(40, self.y, 900)
        if(win32api.GetAsyncKeyState(0x25) & 0x8000 or win32api.GetAsyncKeyState(0x26) & 0x8000
        or win32api.GetAsyncKeyState(0x27) & 0x8000 or win32api.GetAsyncKeyState(0x28) & 0x8000):
            if win32api.GetAsyncKeyState(0x25) & 0x8000:
                self.x-= 400 * gfw.delta_time
            if win32api.GetAsyncKeyState(0x27) & 0x8000:
                self.x += 400 * gfw.delta_time
            if win32api.GetAsyncKeyState(0x26) & 0x8000: # UP
                self.y +=400 * gfw.delta_time
            if win32api.GetAsyncKeyState(0x28) & 0x8000: #DOWN
                self.y -= 400 * gfw.delta_time
        else:
            playerState = 0
        self.time=(self.time + 1) % 50
        if win32api.GetAsyncKeyState(0x25) & 0x8000 and self.time >= 48:
            self.frame -= 1
        if win32api.GetAsyncKeyState(0x27) & 0x8000 and self.time >= 48:
            self.frame += 1        
        if self.frame <= 0: self.frame = 0
        if self.frame>=6: self.frame = 6
    
    def draw(self):
        self.image.clip_draw(3 * 33, 0, 33, 33, self.x, self.y,80, 80)