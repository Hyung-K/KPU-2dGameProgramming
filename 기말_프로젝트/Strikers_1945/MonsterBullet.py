from pico2d import *
import random
import gfw
import Player

name = 'PlaneBullet'

class PlaneBullet:
	image = None

	def __init__(self, x, y, index, speed = 500):
		self.index = index
		self.speed = speed
		self.x, self.y = x, y
		self.frame = 0
		self.radius = 7.5
		self.isDead = False

		if PlaneBullet.image == None:
			PlaneBullet.image = load_image('res/PlaneBullet.png')

	def update(self):
		self.y -= self.speed * gfw.delta_time
		self.frame = (self.frame + 1) % 8

		if self.isDead == True or self.y <= 0 or self.x < 0 or self.x > 720:
			self.remove()

	def draw(self):
		self.image.clip_draw(8 * self.frame, 0, 8, 10, self.x, self.y, 15, 15)

	def remove(self):
		self.image.remove(self)

class PlaneBullet2:
	image = None

	def __init__(self, x, y, index, deltaX, speed=500):
		self.speed = speed
		self.x, self.y = x, y
		self.deltaX = deltaX
		self.radius = 10
		self.index = index
		self.isDead = False
		self.frame = 0
		if PlaneBullet2.image == None:
			PlaneBullet2.image = load_image('res/Bullet.png')

	def update(self):
		self.x += self.deltaX * gfw.delta_time
		self.y -= self.speed * gfw.delta_time
		self.frame = (self.frame + 1) % 2

		if self.isDead == True or self.y <= 0 or self.x < 0 or self.x > 720:
			self.remove()

	def draw(self):
		self.image.clip_draw(23 * self.frame, 0, 23, 41, self.x, self.y, 20, 30)

	def remove(self):
		gfw.world.remove(self)

class PlaneBullet3:
	image = None

	def __init__(self, x, y, deltaX, index, speed = 500):
		self.index = index
		self.speed = speed
		self.x, self.y = x, y
		self.deltaX = deltaX
		self.radius = 7.5
		self.isDead = False
		self.frame = 0
		if PlaneBullet3.image is None:
			PlaneBullet3.image = load_image('res/PlaneBullet.png')

	def update(self):
		self.x += self.deltaX * gfw.delta_time
		self.y -= self.speed * gfw.delta_time
		self.frame = (self.frame + 1) % 8
		if self.isDead is True or self.y <= 0 or self.x < 0 or self.x > 720:
			self.remove()

	def draw(self):
		self.image.clip_draw(8 * self.frame, 0, 8, 10, self.x, self.y, 15, 15)

	def remove(self):
		gfw.world.remove(self)

class Monster1_Bullet:
	image = None

	def __init__(self, x, y, index, speed = 500):
		self.index = index
		self.speed = speed
		self.x, self.y = x, y
		self.radius = 7.5
		self.isDead = False
		self.frame = 0

		for player in gfw.world.objects_at(gfw.layer.Player):
			self.random_delta = random.randint(60, 100) / 100
			self.deltaX, self.deltaY = x - player.x, y - player.y
		if Monster1_Bullet.image is None:
			Monster1_Bullet.image = load_image('res/PlaneBullet.png')

	def update(self):
		self.x -= self.deltaX * gfw.delta_time * self.random_delta
		self.y -= self.deltaY * gfw.delta_time * self.random_delta
		self.frame = (self.frame + 1) % 8
		if self.isDead == True or self.y <= 0 or self.x < 0 or self.x > 720:
			self.remove()

	def draw(self):
		self.image.clip_draw(8 * self.frame, 0, 8, 10, self.x, self.y, 15, 15)

	def remove(self):
		gfw.world.remove(self)