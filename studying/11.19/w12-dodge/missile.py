from pico2d import *
import gfw
MOVE_PPS = 200
class Missile:
	SIZE = 60
	def __init__(self,pos,delta):
		self.pos = pos
		self.delta = delta
		self.image = gfw.image.load('res/missile.png')
	def update(self):
		x,y = self.pos
		dx,dy = self.delta
		x+=dx *MOVE_PPS*gfw.delta_time
		y+=dy*MOVE_PPS*gfw.delta_time
		
		if not self.in_boundary():
			gfw.world.remove(self)
		self.pos = x,y
	def draw(self):	
		self.image.draw(*self.pos)		
	
	def in_boundary(self):
		x,y = self.pos
		if x<-Missile.SIZE:return False
		if y<-Missile.SIZE:return False
		if x>get_canvas_width()+Missile.SIZE: return False
		if y>get_canvas_width()+Missile.SIZE: return False
		return True