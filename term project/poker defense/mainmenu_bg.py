from pico2d import *
import gfw

def init():
	global menu
	menu = gfw.image.load('res/main_menu.png')

def draw():
	x,y = get_canvas_width() // 2,get_canvas_height() // 2
	menu.draw(x,y)

def update():
	pass
