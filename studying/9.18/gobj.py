from pico2d import *
import random
class Grass:
	def __init__(self):
		self.image = load_image('../resource/grass.png')
	def draw(self):
		self.image.draw(400,30)
	def update(seft):
	#다른 객체와 함께 불리기 위해 기능이 없지만 함수를 만드는게 필요할수도 있다.
		pass

class Boy:
	# def __init__(self,pos,delta):
	# 	#객체가 생성되면 반드시 생성(생성자,constructor)
	# 	self.x,self.y = pos
	# 	self.dx,self.dy =delta
	# 	self.fidx = 0
	# 	self.image = load_image('../resource/run_animation.png')
	def __init__(self):
		#객체가 생성되면 반드시 생성(생성자,constructor)
		self.x = random.randint(100,300)
		self.y = random.randint(100,300)
		self.dx,self.dy =random.random(),random.random()
		self.fidx = random.randint(0,7)
		self.image = load_image('../resource/run_animation.png')
	def draw(self):
		self.image.clip_draw(self.fidx*100,0,100,100,self.x,self.y,)
	def update(self):
		self.x += self.dx
		self.y += self.dy
		self.fidx = (self.fidx+1)%8
if __name__=="__main__":
	print("Running test code!!")
	pass