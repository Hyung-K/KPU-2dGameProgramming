from pico2d import*
import gfw

class Lager_Energy:
	image = None
	image2 = None

	def __init__(self, x, y):
		self.x, self.y = x, y
		if Lager_Energy.image is None:
			Lager_Energy.image = load_image('res/Energy_bar.png')
		if Lager_Energy.image2 is None:
			Lager_Energy.image2 = load_image('res/Energy.png')

	def update(self):
		pass

	def draw(self):
		for player in gfw.world.objects_at(gfw.layer.Player):
			self.image.draw(self.x, self.y, 340, 28)
			self.image2.clip_draw(0, 0, 304, 28, self.x - 152 + player.gage * 1.52, self.y, player.gage * 3.04, 14)

class Life:
	image = None
	def __init__(self):
		if Life.image is None:
			Life.image = load_image('res/Life.png')
	def update(self):
		pass
	def draw(self):
		for player in gfw.world.objects_at(gfw.layer.Player):
			for n in range(player.life):
				self.image.draw(660, 10 + 20 * n, 30, 40)


class Score:
	image = [None, None, None, None, None]

	def __init__(self):
		if Score.image[0] is None:
			for i in range(5):
				Score.image[i] = load_image('res/Count.png')
			self.Score = 0
			self.preScore = 0
			self.index = [0, 0, 0, 0, 0]

	def Add_Score(self, x):
		self.Score += x

	def Notify(self):
		self.index[0] = self.Score / 10000
		self.index[1] = (self.Score % 10000) / 1000
		self.index[2] = (self.Score % 1000) / 100
		self.index[3] = (self.Score % 100) / 10
		self.index[4] = self.Score & 10
		print(self.index[2])

	def update(self):
		if self.preScore != self.Score:
			self.Notify()

		self.preScore = self.Score

	def draw(self):
		for i in range(5):
			self.image[i].clip_draw(int(self.index[i]) * 60, 0, 60, 78, 100 + i *10, 940, 13, 30)

class Final_Score:
	image = None
	image2 = [None, None, None, None, None]

	def __init__(self):
		self.index = [0, 0, 0, 0, 0]

		if Final_Score.image2[0] is None:
			for i in range(5):
				Final_Score.image2[i] = load_image('res/Count.png')
		self.x, self.y = 720 / 2, 650
		if Final_Score.image is None:
			Final_Score.image = load_image('res/Score.png')

		for Score in gfw.world.objects_at(gfw.layer.UI):
			self.index[0] = Score / 10000
			self.index[1] = (Score % 10000) / 1000
			self.index[2] = (Score % 1000) / 100
			self.index[3] = (Score % 100) / 10
			self.index[4] = Score % 10

	def update(self):
		pass

	def draw(self):
		self.image.draw(self.x, self.y, 720, 350)
		for i in range(5):
			self.image2[i].clip_draw(int(self.index[i]) * 60, 0, 60, 78, 500 + i * 30, 570, 20, 40)

class Player_Bomb:
	image = None

	def __init__(self):
		if Player_Bomb.image is None:
			Player_Bomb.image = load_image('res/Item_Bomb2.png')

	def update(self):
		pass

	def draw(self):
		for player in gfw.world.objects_at(gfw.layer.Player):
			for n in range(player.bombNo):
				self.image.draw(690, 10 + 20 * n,30, 20)