from pico2d import*
import gfw
from gobj import *

name = 'Bullet'

class Bullet(): 
	image = [None, None, None, None]

	def __init__(self):
		pass
	def __init__(self, x, y, speed = 720):
		self.x, self.y = x, y
		self.dy = speed

		if self.image[0] == None:
			self.image[0] = load_image('res/Bullet_Eg_a.png')
		if self.image[1] == None:
			self.image[1] = load_image('res/Bullet_Eg_b.png')
		if self.image[2] == None:
			self.image[2] = load_image('res/Bullet_Eg_c.png')
		if self.image[3] == None:
			self.image[3] = load_image('res/Bullet_Eg_d.png')

	def update(self):
		self.y += self.dy * gfw.delta_time

		if self.y > get_canvas_height() + 20:
			self.remove()

	def draw(self):
		self.image[0].draw(self.x - 7, self.y + 10, 120, 120)

	def remove(self):
		gfw.world.remove(self)