import random
from pico2d import*
import gfw

def rand(n):
	return n * random.uniform(0.9, 1.1)

def add_point(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return x1 + x2, y1 + y2

def move_obj(obj):
	obj.pos = add_point(obj.pos, obj.delta)

def collision_box(a, b):
	(la, ba, ra, ta) = a.get_bb()
	(lb, bb, rb, tb) = b.get_bb()

	if la > rb: return False
	if ra < lb: return False
	if ba > tb: return False
	if ta < bb: return False
	return True

def draw_collision_box():
	for obj in gfw.world.all_objects():
		if hasattr(obj, 'get_bb'):
			draw_rectangle(*obj.get_bb())

if __name__ == "__main__":
	print("This file is not supposed to be executed directly.")