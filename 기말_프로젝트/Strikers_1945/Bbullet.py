from pico2d import *

import gfw
import Effect

class Bbullet:
	image = None

	def __init__(self):
		self.Number = number
		self.x, self.y = x, y
		self.deltaX, self.deltaY = deltaX, deltaY
		self.radius = 10
		self.isdead = False
		self.frame = 0
		self.lifetime = random.randint(100, 300) / 100