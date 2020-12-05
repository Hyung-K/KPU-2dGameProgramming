import gfw
import pickle
import time

FILE_NAME = 'score_data.pickle'
scores = []
Max_Score_Cnt = 5
last_rank = -1

class Entry:
    def __init__(self, score):
        self.score = score
        self.time = time.time()

def load():
    global font, image
    font = gfw.font.load('res/Press_Start_2P.ttf', 20)

    global scores
    try:
        f = open(FILE_NAME, "rb")
        scores = pickle.load(f)
        f.close()
    except:
        print("No HighScore File")

def save():
    f = open(FILE_NAME, "wb")
    pickle.dump(scores, f)
    f.close()

def add(score):
    global scores, last_rank
    entry = Entry(score)
    insrtd = False

    for i in range(len(scores)):
        e = scores[i]
        if e.score < entry.score:
            scores.insert(i, entry)
            insrtd = True
            last_rank = i + 1
            break

    if not insrtd:
        scores.append(entry)
        last_rank = len(scores)

    if len(scores) > Max_Score_Cnt:
        scores.pop(-1)

    if last_rank <= Max_Score_Cnt:
        save()

def draw():
    global font, last_rank
    n =1
    y = 600
    for e in scores:
        str = "{:d}{:7.1f}".format(n, e.score)
        color = (0, 0, 0) if n == last_rank else (0, 0, 0)
        font.draw(10, y, str, color)
        font.draw(260, y, time.asctime(time.localtime(e.time)), color)
        y -= 30
        n += 1

def update():
    pass
