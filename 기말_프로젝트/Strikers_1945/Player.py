from pico2d import *
import gfw
from gobj import *
import win32api
import Bullet 

class Player():
    def __init__(self):
        self.x, self.y = 0, 90
        self.image = load_image('res/Player_T.png')
        self.frame = 3    # speed
        self.time = 0
        self.interval = 0
        self.playerState = 0

        self.life = 4
        self.bombNo = 2     # 필살기
        self.gage = 0
        self.Power = 0
        self.lagerTime = 0
        self.soundDelta = 0
        self.isShield = False
        self.shieldTime = 0

        self.SMode = False

    def fire(self):
        if win32api.GetAsyncKeyState(0x20) & 0x8000 and self.interval>=1:  # space
            self.interval = 0
            bullet = Bullet.Bullet(self.x, self.y + 20)
            gfw.world.add(gfw.layer.Bullet,bullet)

    def update(self):
        self.fire()
        self.interval += (20 * gfw.delta_time)
        self.x = clamp(40, self.x, 700)
        self.gage = clamp(0, self.gage, 100)
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