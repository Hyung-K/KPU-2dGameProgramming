from pico2d import *

import random
import gfw
import gobj
from Player import Player
import Monster
import Monster2
import UI
import Effect

bisPlaneMake = True
RedPlaneTerm = 0
MakeTerm = 0
SmlBoss_MakeTerm = 0

SmlBossCnt = 2
MidBossCnt = 1
FinalBossCnt = 1

Time = 0
bisMidBossDead = False

def enter():
	gfw.world.init(['Player', 'Bullet', 'Monster', 'MonsterBullet', 'UI', 'Effect', 'Item', 'Laser', 'Hyperion'])
	global player, score
	player = Player.Player()
	gfw.world.add(gfw.layer.Player, player)

	score = UI.Score()
	life = UI.Life()
	gfw.world.add(gfw.layer.UI, score)
	gfw.world.add(gfw.layer.UI, UI.Laser_Energy(160, 30))
	gfw.world.add(gfw.layer.UI, UI.Player_Bomb())
	gfw.world.add(gfw.layer.UI, life)

def update():
	gfw.world.update()
	Player_Bullet_Collision()
	Monster_Bullet_Collision()

	global MakeTerm, RedPlaneTerm, bisPlaneMake
	global Time

	MakeTerm += gfw.delta_time * 0.5
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

	if RedPlaneTerm >= 4 and FinalBossCnt > 0:
		RedPlaneTerm = 0
		Redplane = Monster2.RedPlane(random.randint(0, 300), 960)
		gfw.world.add(gfw.layer.Monster, Redplane)

	if SmlBoss_MakeTerm > 10 and SmlBossCnt > 0:
		SmlBoss_MakeTerm = 0
		SmlBossCnt -= 1
		S1 = Monster2.MidPlane(1300, 1300, -1)
		gfw.world.add(gfw.layer.Monster, S1)
		S2 = Monster2.MidPlane(-580, 1300, 1)
		gfw.world.add(gfw.layer.Monster, S2)

	if Time > 20 and MidBossCnt > 0:
		MidBossCnt -= 1
		BAP = Monster2

def Monster_Bullet_Collision():
	global player, score
	for Monster in gfw.world.objects_at(gfw.layer.Monster):
		for MonsterBullet in gfw.world.objects_at(gfw.layer.MonsterBullet):
			for PlayerBullet in gfw.world.objects_at(gfw.layer.Bullet):
				if Monster.x + Monster.RadianX > PlayerBullet.x > Monster.x - Monster.RadianX and Monster.y + Monster.PivotY > PlayerBullet.y > Monster.y - Monster.PivotY:
					PlayerBullet.isDead = True
					Monster.hp -= 0.5 + player.Power * 0.75
					player.gage += 0.5
					score.Add_Score(random.randint(3, 7))
					PlayerBullet.isDead = True
					Pp = Effect.Effect(PlayerBullet.x + random.randint(-15, 15),
									   PlayerBullet.y + random.randint(-15, 15), 30, 27, 30, 27, 12, 0)
					gfw.world.add(gfw.layer.Effect, Pp)

def Player_Bullet_Collision():
	global player, score
	for Monster in gfw.world.objects_at(gfw.layer.Monster):
		for MonsterBullet in gfw.world.objects_at(gfw.layer.MonsterBullet):
			for PlayerBullet in gfw.world.objects_at(gfw.layer.Bullet):
				dist = math.sqrt((player.x - MonsterBullet.x) ** 2 + (player.y - MonsterBullet.y) ** 2)
				if dist <= MonsterBullet.radius and player.isShield is False:
					MonsterBullet.isdead = True
					if player.SMode is False:
						player.Life -= 1

					Cp = Effect.Effect(player.x + random.randint(-20, 20), player.y + random.randint(-20, 20), 128, 128, 250, 250, 64, 5, 0.3)
					gfw.world.add(gfw.layer.Effect, Cp)

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