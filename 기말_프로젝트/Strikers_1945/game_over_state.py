from pico2d import *
import gfw

import Highscore

def enter():
    global game_over_image, bgm, font
    gfw.world.init(['highscore'])
    game_over_image = gfw.load_image('res/game_over.png')
    bgm = load_music('Sound/highscore.mp3')
    bgm.set_volume(50)
    bgm.repeat_play()
    font = gfw.font.load('res/Press_Start_2P.ttf', 20)
    Highscore.load()
    gfw.world.add(gfw.layer.highscore, Highscore)

def update():
    gfw.world.update()

def draw():
    game_over_image.draw(360, 480, 720, 960)
    gfw.world.draw()

def handle_event(e):
    global bgm
    if e.type == SDL_QUIT:
        gfw.quit()

    else:
        if (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            bgm.stop()
            gfw.quit()

        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_r):
            bgm.stop()
            gfw.pop()

def exit():
    global bgm
    del bgm

def pause():
    pass

def resume():
    pass

if __name__ == '__main__':
    gfw.run_main()