from pico2d import *
from bg import VertScrollBackground
import gfw
import random

import Player
import Monster
import Monster2
import UI
import Effect
import Ship
import SoundM
import Highscore
import game_over_state

canvas_width = 720
canvas_height = 960
STATE_IN_GAME, STATE_GAME_OVER = range(2)

def end_game():
    global state, Sound, score
    state = STATE_GAME_OVER
    Sound.bgm1.stop()
    Sound.bgm2.repeat_play()
    Highscore.add(score)
    gfw.change(game_over_state)

def enter():
    gfw.world.init(
        ['bg', 'Player', 'Boss', 'Bullet', 'Monster', 'MonsterBullet', 'UI', 'Effect', 'Item', 'Laser', 'Hyperion'])
    global player, score, Sound, state
    global font
    state = STATE_IN_GAME
    player = Player.Player()
    font = gfw.font.load('res/Press_Start_2P.ttf', 20)
    Sound = SoundM
    Sound.init()
    Sound.bgm1.repeat_play()
    gfw.world.add(gfw.layer.Player, player)
    life = UI.Life()
    score = 0
    gfw.world.add(gfw.layer.UI, UI.Laser_Energy(160, 30))
    gfw.world.add(gfw.layer.UI, UI.Player_Bomb())
    gfw.world.add(gfw.layer.UI, life)

    bg = VertScrollBackground('Map_2.png')
    bg.speed = 40
    gfw.world.add(gfw.layer.bg, bg)
    Highscore.load()

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
    global player, score, Sound
    for Monster in gfw.world.objects_at(gfw.layer.Monster):
        for MonsterBullet in gfw.world.objects_at(gfw.layer.MonsterBullet):
            for PlayerBullet in gfw.world.objects_at(gfw.layer.Bullet):
                if Monster.x + Monster.radianX > PlayerBullet.x > Monster.x - Monster.radianX and Monster.y + Monster.pivotY > PlayerBullet.y > Monster.y - Monster.pivotY:
                    PlayerBullet.isDead = True
                    Monster.hp -= 0.5 + player.power * 0.75
                    player.Gage += 0.1
                    score += 1
                    PlayerBullet.isDead = True
                    Pp = Effect.Effect(PlayerBullet.x + random.randint(-15, 15),
                                       PlayerBullet.y + random.randint(-15, 15),
                                       30, 27, 30, 27, 12, 0)
                    gfw.world.add(gfw.layer.Effect, Pp)


def PlayerBullet_Collision():
    global player, Sound, state
    for Monster in gfw.world.objects_at(gfw.layer.Monster):
        for MonsterBullet in gfw.world.objects_at(gfw.layer.MonsterBullet):
            dist = math.sqrt((player.x - MonsterBullet.x) ** 2 + (player.y - MonsterBullet.y) ** 2)
            if dist <= MonsterBullet.radius and player.isShield is False:
                MonsterBullet.isDead = True
                Sound.playSound(14, 40)
                if player.SMode is False:
                    player.isShield = True

                    Cp = Effect.Effect(player.x + random.randint(-20, 20),
                                       player.y + random.randint(-20, 20),
                                       128, 128, 250, 250, 64, 5, 0.3)
                    gfw.world.add(gfw.layer.Effect, Cp)
                    if player.life <= 0:
                        state = STATE_GAME_OVER
                        return True

def MTime():
    global MakeTerm, RedPlaneTerm, bisPlaneMake, SmlBoss_MakeTerm, SmlBossCnt, MidBossCnt, FnlBossCnt, bisMidBossDead
    global Time, boss, score, Sound

    MakeTerm += gfw.delta_time * 0.7
    RedPlaneTerm += gfw.delta_time * 0.3
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
        Sound.bgm1.stop()
        Sound.bgm3.repeat_play()
        score += 2000
        FnlBossCnt -= 1
        boss = Ship.BossShip(1400, 860)
        gfw.world.add(gfw.layer.Boss, boss)
        bisPlaneMake = False

    if Ship.checkDead:
        score += 5000
        Sound.bgm4.stop()
        return True

def update():
    if state != STATE_IN_GAME:
        return
    MonsterBullet_Collision()
    PlayerBullet_Collision()
    gfw.world.update()
    ends = PlayerBullet_Collision()
    clear = MTime()
    if ends or clear:
        end_game()

def draw():
    gfw.world.draw()
    score_pos = 30, get_canvas_height() - 30
    font.draw(*score_pos, 'Score: %d' % score, (255, 255, 255))

def handle_event(e):
    global player
    if e.type == SDL_QUIT:
        gfw.quit()

    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

def exit():
    global Sound
    Sound.Delete_AllLst()

if __name__ == '__main__':
    gfw.run_main()
