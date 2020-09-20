from pico2d import *
import helper

open_canvas()

def handle_events():
	global running,mx,my,speed,start,now
	#global pos
	#global target
	evts = get_events()
	for e in evts:
		if e.type == SDL_QUIT:
			running = False
		elif e.type==SDL_KEYDOWN:
			if e.key == SDLK_ESCAPE:
				running = False
		elif e.type == SDL_MOUSEBUTTONDOWN:	
				if start==False:
				#처음값은 리스트를 추가하고 현재좌표 값을 1증가시킴
					now+=1
					speed=1
					start = True
				else:
					speed = 2
				#이후에는 리스트에 값만을 추가.
				mx.append(e.x)
				my.append(get_canvas_height()-e.y-1)
				
					
					

img = load_image('../res/run_animation.png')
gra = load_image('../res/grass.png')\

now = 0#현재 좌표를 가리키는 함수
x = 30
y = 80
dx = 0
dy = 0
mx = [30]
my = [80]
speed = 1
start = False
running = True
frame = 0
while running:
	clear_canvas()
	gra.draw(400,30)
	img.clip_draw(frame*100,0,100,100,x,y)
	#두개의 이미지를 그려줌
	update_canvas()
	frame = (frame+1) % 8	
	handle_events()	
	dx,dy = helper.delta([x,y], [mx[now],my[now]], speed)	
	if dx==0 and dy == 0 and start == True:
		speed = 1
		now+=1
		if len(mx)==now:
		#도착시했고 리스트의 다음값이 없을땐 now에 값을 더하지 않음. 리스트의 다음값이 없기때문에 다음좌표를 가리킬수 없음.
			now-=1	
	[x,y],done = helper.move_toward([x,y],[dx,dy],[mx[now],my[now]])
	delay(0.03)	
	
	

close_canvas()
