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
