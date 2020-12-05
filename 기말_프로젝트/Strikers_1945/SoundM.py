from pico2d import *

def init():
    global soundLst, bgm1, bgm2, bgm3, bgm4

    bgm1 = load_music('Sound/main.mp3')
    bgm1.set_volume(40)
    bgm2 = load_music('Sound/GameOver.mp3')
    bgm2.set_volume(40)
    bgm3 = load_music('Sound/boss.mp3')
    bgm3.set_volume(40)
    bgm4 = load_music('Sound/missionComplete!.mp3')
    bgm4.set_volume(40)

    explode1 = load_wav('Sound/Explode_Bomb.wav')
    explode2 = load_wav('Sound/Explode_Guide.wav')
    explode3 = load_wav('Sound/Explode_StaticAI.wav')

    bossExplosion1 = load_wav('Sound/BossExplosion_1.wav')
    bossExplosion2 = load_wav('Sound/BossExplosion_2.wav')
    bossExplosion3 = load_wav('Sound/BossExplosion_3.wav')
    bossExplosion4 = load_wav('Sound/BossExplosion_4.wav')
    bossExplosion5 = load_wav('Sound/BossExplosion_5.wav')

    bullet = load_wav('Sound/Bullet.wav')
    blueBulletExplosion = load_wav('Sound/BlueBullet_Explosion.wav')
    bullet_Scout = load_wav('Sound/Bullet_Scout.wav')

    powerUp = load_wav('Sound/PowerUp.wav')
    powerDown = load_wav('Sound/PowerDown.wav')
    scoreUp = load_wav('Sound/ScoreUp.wav')
    lifeExplosion = load_wav('Sound/LifeExplosion.wav')

    soundLst = [explode1, explode2, explode3, bossExplosion1, bossExplosion2,
                bossExplosion3, bossExplosion4, bossExplosion5, powerUp, powerDown,
                scoreUp, bullet, blueBulletExplosion, bullet_Scout, lifeExplosion]

    explode1.set_volume(30)
    explode2.set_volume(30)
    explode3.set_volume(30)

    for i in range(3, 10):
        soundLst[i].set_volume(45)
    soundLst[11].set_volume(40)
    soundLst[12].set_volume(60)
    soundLst[13].set_volume(60)
    soundLst[14].set_volume(80)

def playSound(number, volume):
    global soundLst
    soundLst[number].set_volume(volume)
    soundLst[number].play(1)

def playSound2(number, volume):
    global soundLst
    soundLst[number].set_volume(volume)
    soundLst[number].play(1)

def Delete_AllLst():
    global soundLst, bgm1, bgm2, bgm3, bgm4
    del bgm1
    del bgm2
    del bgm3
    del bgm4
    for obj in soundLst:
        del(obj)