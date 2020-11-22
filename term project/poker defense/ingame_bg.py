from pico2d import *
import gfw

def init():
	global tile_map
	tile_map = gfw.image.load('res/tile_map.png')

def draw():
	x,y = get_canvas_width() // 2,get_canvas_height() // 2
	tile_map.draw(x,y)

def update():
	pass
