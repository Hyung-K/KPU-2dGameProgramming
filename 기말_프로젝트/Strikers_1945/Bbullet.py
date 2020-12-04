from pico2d import *

import gfw
import random
import math
import Effect

class Bbullet2:
	image = None

	def __init__(self):
		self.Number = number
		self.x, self.y = x, y
		self.deltaX, self.deltaY = deltaX, deltaY
		self.radius = 10
		self.isdead = False
		self.frame = 0
		self.lifetime = random.randint(100, 300) / 100
		self.deathtime = 0
		self.index = 0

		if Bbullet2.image is None:
			Bbullet2.image = load_image('res/Blue_Bullet2.png')

	def Bullet_lifetime(self):
		if self.isdead is True or self.y <= 0 or self.x < 0 or self.x > 740:
			self.remove()

	def update(self):
		self.Bullet_lifetime()
		self.x += gfw.delta_time * self.deltaX * 2
		self.y += gfw.delta_time * self.deltaY * 2

		self.frame += gfw.delta_time * 10
		if self.frame >= 16:
			self.frame = 0

		if self.isdead is True or self.y <= 0 or self.x < -10 or self.x > 740:
			if self.Number > 0:
				bEf = Effect.Effect(self.x, self.y, 80, 80, 100, 100, 10, 7, 0.5)
				gfw.world.add(gfw.layer.Effect, bEf)
				BB = Bbullet2(self.x, self.y, self.Number - 1, 0, 100)
				gfw.world.add(gfw.layer.MonsterBullet, BB)
				BB1 = Bbullet2(self.x, self.y, self.Number - 1, 50 * math.sqrt(2), 50 * math.sqrt(2))
				gfw.world.add(gfw.layer.MonsterBullet, BB1)
				BB2 = Bbullet2(self.x, self.y, self.Number - 1, 100, 0)
				gfw.world.add(gfw.layer.MonsterBullet, BB2)
				BB3 = Bbullet2(self.x, self.y, self.Number - 1, 50 * math.sqrt(2), -50 * math.sqrt(2))
				gfw.world.add(gfw.layer.MonsterBullet, BB3)
				BB4 = Bbullet2(self.x, self.y, self.Number - 1, 0, -100)
				gfw.world.add(gfw.layer.MonsterBullet, BB4)
				BB5 = Bbullet2(self.x, self.y, self.Number - 1, -50 * math.sqrt(2), -50 * math.sqrt(2))
				gfw.world.add(gfw.layer.MonsterBullet, BB5)
				BB6 = Bbullet2(self.x, self.y, self.Number - 1, -100, 0)
				gfw.world.add(gfw.layer.MonsterBullet, BB6)
				BB7 = Bbullet2(self.x, self.y, self.Number - 1, -50 * math.sqrt(2), 50 * math.sqrt(2))
				gfw.world.add(gfw.layer.MonsterBullet, BB7)
			self.remove()

	def draw(self):
		self.image.clip_draw(450 * int(self.frame), 0, 450, 450, self.x, self.y, 20, 20)

	def remove(self):
		gfw.world.remove(self)