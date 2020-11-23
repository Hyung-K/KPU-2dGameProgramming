from pico2d import *
import win32api
import random
import gfw
import gobj
from Player import Player
import Monster     
import UI
import Effect

bisAirPlaneMake = True
RedAirPlaneTerm = 0
MakeTerm = 0

def enter():
	gfw.world.init(['Player','Bullet','Monster','MonsterBullet', 'UI','Effect'])
	global player, score, life
	player = Player()
	gfw.world.add(gfw.layer.Player, player)

	score = UI.Score()
	life = UI.Life()
	gfw.world.add(gfw.layer.UI, score)
	gfw.world.add(gfw.layer.UI, UI.Lager_Energy(160, 30))
	gfw.world.add(gfw.layer.UI, UI.Player_Bomb())
	gfw.world.add(gfw.layer.UI, life)

def update():
	gfw.world.update()
	Player_Bullet_Collision()
	Monster_Bullet_Collision()

	global MakeTerm, RedAirPlaneTerm, bisAirPlaneMake
	global Time

	MakeTerm += gfw.delta_time * 0.5
	if MakeTerm >= 1 and bisAirPlaneMake is True:
		MakeTerm = 0

		Lp = Monster.LeftPlane1(random.randint(0, 720), 960)
		Rp = Monster.RightPlane1(random.randint(0, 720), 960)
		gfw.world.add(gfw.layer.Monster, Lp)
		gfw.world.add(gfw.layer.Monster, Rp)

def Monster_Bullet_Collision():
	global player, score
	for Monster in gfw.world.objects_at(gfw.layer.Monster):
		for MonsterBullet in gfw.world.objects_at(gfw.layer.MonsterBullet):
			for PlayerBullet in gfw.world.objects_at(gfw.layer.Bullet):
				if Monster.x + Monster.radianX > PlayerBullet.x > Monster.x - Monster.radianX and Monster.y + Monster.pivotY > PlayerBullet.y > Monster.y - Monster.pivotY:
					Monster.hp -= 2 + player.Power * 0.75
					player.gage += 0.5
					score.Add_Score(random.randint(3, 7))
					PlayerBullet.isdead = True
					p = Effect.Effect(PlayerBullet.x + random.randint(-15, 15), PlayerBullet.y + random.randint(-15, 15), 30, 27, 30, 27, 12.0)
					gfw.world.add(gfw.layer.Effect, p)

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

					p = Effect.Effect(player.x + random.randint(-20, 20), player.y + random.randint(-20, 20), 128, 128, 250, 250, 64, 5, 0.3)
					gfw.world.add(gfw.layer.Effect, p)

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