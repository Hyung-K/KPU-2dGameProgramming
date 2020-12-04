from pico2d import *
import gfw
import Player
import Effect

name = 'item'

class Item_Bomb():
	image = None

	def __init__(self,x,y):
		self.x, self.y = x, y
		self.frame = 0
		self.state1 = 'L'
		self.state2 = 'T'

		if Item_Bomb.image == None:
			Item_Bomb.image = load_image('res/Item_Bomb.png')

	def Item_Move(self):
		if self.state1 == 'L':
			self.x -= gfw.delta_time * 200

			if self.x <= 0:
				self.state1 = 'R'

		elif self.state1 == 'R':
			self.x += gfw.delta_time * 200

			if self.x >= 720:
				self.state1 = 'L'

		if self.state2 == 'T':
			self.y += gfw.delta_time * 400:

			if self.y >= 960:
				self.state2 = 'B'

		elif self.state2 == 'B':
			self.y -= gfw.delta_time * 400

			if self.y <= 0:
				self.state2 = 'T'

	def update(self):
		for Player in gfw.world.objects_at(gfw.layer.Player):
			distance = math.sqrt((self.Player.x - self.x) ** 2 + (self.Player.y - self.y) ** 2)

			if distance < 30:
				Pp = Effect.Effect(self.x, self.y, 144, 100, 80, 50, 8, 3)
				gfw.world.add(gfw.layer.Effect, Pp)

				if self.Player.BombNo < 5:
					self.Player.BombNo += 1
				self.remove();
			self.Item_Move()

			self.frame = (self.frame + gfw.delta_time * 6) % 4

	def draw(self):
		self.image.clip_draw(int(self.frame) * 54, 0, 54, 32, self.x, self.y, 50, 30)

	def remove(self):
		gfw.world.remove(self)