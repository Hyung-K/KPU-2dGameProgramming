from pico2d import *
from bg import VertScrollBackground
import gfw
import random

import title_state
import Player
import Monster
import Monster2
import UI
import Effect
import Ship

def enter():
    gfw.world.init(['bg', 'Player', 'Boss', 'Bullet', 'Monster', 'MonsterBullet', 'UI', 'Effect', 'Item', 'Laser', 'Hyperion'])
    global player, score
    player = Player.Player()
    gfw.world.add(gfw.layer.Player, player)
    score = UI.Score()
    life = UI.Life()
    gfw.world.add(gfw.layer.UI, score)
    gfw.world.add(gfw.layer.UI, UI.Laser_Energy(160, 30))
    gfw.world.add(gfw.layer.UI, UI.Player_Bomb())
    gfw.world.add(gfw.layer.UI, life)

    bg = VertScrollBackground('Map_2.png')
    bg.speed = 50
    gfw.world.add(gfw.layer.bg, bg)

    global bisPlaneMake, MakeTerm, RedPlaneTerm, SmlBoss_MakeTerm, SmlBossCnt, MidBossCnt, FnlBossCnt, Time, bisMidBossDead
    bisPlaneMake = True
    MakeTerm = 0
    RedPlaneTerm = 0
    SmlBoss_MakeTerm = 0
    SmlBossCnt = 2
    MidBossCnt = 1
    FnlBossCnt = 1
    Time = 0
    bisMidBossDead = False

def MonsterBullet_Collision():
    global player, score
    for Monster in gfw.world.objects_at(gfw.layer.Monster):
        for MonsterBullet in gfw.world.objects_at(gfw.layer.MonsterBullet):
            for PlayerBullet in gfw.world.objects_at(gfw.layer.Bullet):
                if Monster.x + Monster.radianX > PlayerBullet.x > Monster.x - Monster.radianX and Monster.y + Monster.pivotY > PlayerBullet.y > Monster.y - Monster.pivotY:
                    PlayerBullet.isDead = True
                    Monster.hp -= 0.5 + player.power * 0.75
                    player.Gage += 0.5
                    score.Add_Score(random.randint(3, 7))
                    PlayerBullet.isDead = True
                    Pp = Effect.Effect(PlayerBullet.x + random.randint(-15, 15),
                                       PlayerBullet.y + random.randint(-15, 15),
                                       30, 27, 30, 27, 12, 0)
                    gfw.world.add(gfw.layer.Effect, Pp)

def PlayerBullet_Collision():
    global player
    for Monster in gfw.world.objects_at(gfw.layer.Monster):
        for MonsterBullet in gfw.world.objects_at(gfw.layer.MonsterBullet):
            dist = math.sqrt((player.x - MonsterBullet.x) ** 2 + (player.y - MonsterBullet.y) ** 2)
            if dist <= MonsterBullet.radius and player.isShield is False:
                MonsterBullet.isDead = True
                if player.SMode is False:
                    player.isShield = True
                    player.life -= 1
                
                    Cp = Effect.Effect(player.x + random.randint(-20, 20),
                                       player.y + random.randint(-20, 20),
                                       128, 128, 250, 250, 64, 5, 0.3)
                    gfw.world.add(gfw.layer.Effect, Cp)

def MTime():
    global MakeTerm, RedPlaneTerm, bisPlaneMake, SmlBoss_MakeTerm, SmlBossCnt, MidBossCnt, FnlBossCnt, bisMidBossDead
    global Time

    MakeTerm += gfw.delta_time * 0.5
    RedPlaneTerm += gfw.delta_time * 0.5
    SmlBoss_MakeTerm += gfw.delta_time * 1
    Time += gfw.delta_time * 1

    if MakeTerm >= 1 and bisPlaneMake is True:
        MakeTerm = 0
        Lp = Monster.LeftPlane1(random.randint(0, 720), 960)
        Rp = Monster.RightPlane1(random.randint(0, 720), 960)
        gfw.world.add(gfw.layer.Monster, Lp)
        gfw.world.add(gfw.layer.Monster, Rp)
        Bp = Monster2.BluePlane(random.randint(0, 300), 960)
        Wp = Monster2.WhitePlane(1000, random.randint(500, 960))
        gfw.world.add(gfw.layer.Monster, Bp)
        gfw.world.add(gfw.layer.Monster, Wp)

    if RedPlaneTerm >= 4 and FnlBossCnt > 0:
        RedPlaneTerm = 0
        Redp = Monster2.RedPlane(random.randint(0, 300), 960)
        gfw.world.add(gfw.layer.Monster, Redp)
            
    if SmlBoss_MakeTerm > 10 and SmlBossCnt > 0:
        SmlBoss_MakeTerm = 0
        SmlBossCnt -= 1
        Sp1 = Monster2.MidPlane(1300, 1300, -1)
        Sp2 = Monster2.MidPlane(-580, 1300, 1)
        gfw.world.add(gfw.layer.Monster, Sp1)
        gfw.world.add(gfw.layer.Monster, Sp2)
    
    if Time > 40 and MidBossCnt > 0:
        MidBossCnt -= 1
        BAP = Monster2.BigPlane(360, 1160)
        gfw.world.add(gfw.layer.Monster, BAP)

    if Time > 70 and Monster2.checkDead == True and FnlBossCnt > 0:
        FnlBossCnt -= 1
        boss = Ship.BossShip(1400, 860)
        gfw.world.add(gfw.layer.Boss, boss)
        bisPlaneMake = False

def update():
    MonsterBullet_Collision()
    PlayerBullet_Collision()
    gfw.world.update()
    MTime()

def draw():
    gfw.world.draw()
    
def handle_event(e):
    global player
    if e.type == SDL_QUIT:
        gfw.quit()
        
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
