
from pico2d import *
from gobj import *

def handle_events():
	global running;
	#함수내에서 값이 결정되는 변수는 지역변수로 간주
	#반드시 글로벌로 설정해줘야함
	#함수는 동작의 추상화 
	evts = get_events()
	for e in evts:
		if e.type == SDL_QUIT:
			running = False
		elif e.type==SDL_KEYDOWN:
			if e.key == SDLK_ESCAPE:
				running = False
			

open_canvas()


# class Grass:
# 	def __init__(self):
# 		self.image = load_image('../resource/grass.png')
# 	def draw(self):
# 		self.image.draw(400,30)
# 	def update(seft):
# 	#다른 객체와 함께 불리기 위해 기능이 없지만 함수를 만드는게 필요할수도 있다.
# 		pass

# class Boy:
# 	# def __init__(self,pos,delta):
# 	# 	#객체가 생성되면 반드시 생성(생성자,constructor)
# 	# 	self.x,self.y = pos
# 	# 	self.dx,self.dy =delta
# 	# 	self.fidx = 0
# 	# 	self.image = load_image('../resource/run_animation.png')
# 	def __init__(self):
# 		#객체가 생성되면 반드시 생성(생성자,constructor)
# 		self.x = random.randint(100,300)
# 		self.y = random.randint(100,300)
# 		self.dx,self.dy =random.random(),random.random()
# 		self.fidx = random.randint(0,7)
# 		self.image = load_image('../resource/run_animation.png')
# 	def draw(self):
# 		self.image.clip_draw(self.fidx*100,0,100,100,self.x,self.y,)
# 	def update(self):
# 		self.x += self.dx
# 		self.y += self.dy
# 		self.fidx = (self.fidx+1)%8

grass = Grass()
#boy = Boy((0,85),(2,0.1)) #객체 생성 instanciation , 클래스이름()
#boy2 = Boy((0,200),(1,0.05))

#objects = [boy,boy2,ball....]
#리스트를 만들고 for문으로  오브젝트 돌리면 됨.(객체의 다형성)

team = [Boy() for i in range(11)]

		
running = True
while running:
	clear_canvas()
	grass.draw()
	#boy.draw()
	#boy2.draw()
	for boy in team:
		boy.draw()

	update_canvas()

	handle_events()
	for boy in team:
		boy.update()

	grass.update()	
	#boy.update()
	#boy2.update()

	# if boy.x>get_canvas_width():
	# 	running = False

	delay(0.03)	

close_canvas()
