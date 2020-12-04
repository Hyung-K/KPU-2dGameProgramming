from pico2d import *
import gfw
import Effect

class Hyperion_Bullet():
	image = None

	def __init__(self, x, y, dir):
		self.x, self.y = x,y
		self. dir = dir
		self.isDead = False

		if Hyperion_Bullet.image == None:
			Hyperion_Bullet.image = load_image('res/Special_Bullet.png')

	def update(self):
		if self.dir == 0:
			self.y += gfw.delta_time * 720
		elif self.dir == 1:
			self.x -= gfw.delta_time * 720
			self.y += gfw.delta_time * 720
		elif self.dir == 2:
			self.x += gfw.delta_time * 720
			self.y += gfw.delta_time * 720

		if self.x < 0 or self.x > 720 or self.y > 960:
			self.remove()
		if self.isDead == True:
			self.remove()

	def draw(self):
		self.image.clip_draw(self.dir * 42, 0, 40, 48, self.x, self.y, 50, 50)

	def remove(self):
		gfw.world.remove(self)