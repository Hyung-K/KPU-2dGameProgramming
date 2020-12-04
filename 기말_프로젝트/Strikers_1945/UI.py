from pico2d import *
import gfw

class Laser_Energy:
    image1 = None
    image2 = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        if Laser_Energy.image1 is None:
            Laser_Energy.image1 = load_image('res/Energy_bar.png')

        if Laser_Energy.image2 is None:
            Laser_Energy.image2 = load_image('res/Energy.png')

    def update(self):
        pass

    def draw(self):
        for player in gfw.world.objects_at(gfw.layer.Player):
            self.image1.draw(self.x, self.y, 340, 28)
            self.image2.clip_draw(0, 0, 304, 28, self.x-152 + player.Gage * 1.52, self.y, player.Gage * 3.04, 14)

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
                self.image.draw(690, 10 + 20 * n, 30, 20)

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
        self.index =[0, 0, 0, 0, 0]

    def Add_Score(self, x):
        self.Score += x

    def Notify(self):
        self.index[0] = self.Score / 10000
        self.index[1] = (self.Score % 10000) / 1000
        self.index[2] = (self.Score % 1000) / 100
        self.index[3] = (self.Score % 100) / 10
        self.index[4] = self.Score % 10

    def update(self):
        if self.preScore != self.Score:
            self.Notify()

        self.preScore = self.Score

    def draw(self):
        for i in range(5):
            self.image[i].clip_draw(int(self.index[i]) * 60, 0, 60, 78, 100 + i * 10, 940, 13, 30)

class FinalScore:
    image = None
    image2 = [None, None, None, None, None]

    def __init__(self):
        self.index = [0, 0, 0, 0, 0]

        if FinalScore.image2[0] is None:
            for i in range(5):
                FinalScore.image2[i] = load_image('res/Count.png')
        self.x, self.y = 720 / 2, 650

        if FinalScore.image is None:
            FinalScore.image = load_image('res/Score.png')

        for score in gfw.world.objects_at(gfw.layer.CUI):
            self.index[0] = score / 10000
            self.index[1] = (score % 10000) / 1000
            self.index[2] = (score % 1000) / 100
            self.index[3] = (score % 100) / 10
            self.index[4] = score % 10

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y, 720, 350)
        for i in range(5):
            self.image2[i].clip_draw(int(self.index[i]) * 60, 0, 60, 78, 500 + i * 30, 570, 20, 40)