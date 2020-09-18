from pico2d import *

def handle_events():
	global running,dx,x,y
	#함수내에서 값이 결정되는 변수는 지역변수로 간주
	#반드시 글로벌로 설정해줘야함
	evts = get_events()
	for e in evts:
		if e.type == SDL_QUIT:
			running = False
		elif e.type==SDL_KEYDOWN:
			if e.key == SDLK_ESCAPE:
				running = False
			elif e.key == SDLK_LEFT:
				dx -= 1
			elif e.key == SDLK_RIGHT:
				dx +=1
		elif e.type==SDL_KEYUP:
			if e.key == SDLK_LEFT:
				dx += 1
			elif e.key == SDLK_RIGHT:
				dx -= 1
		elif e.type == SDL_MOUSEMOTION:
			x,y = e.x,get_canvas_height()-e.y-1

open_canvas()
img = load_image('../resource/run_animation.png')
gra = load_image('../resource/grass.png')

running = True
x,y = get_canvas_width()//2,80
dx = 0
frame = 0
hide_cursor()
while running and x < 800:
	clear_canvas()

	gra.draw(400,30)
	img.clip_draw(frame*100,0,100,100,x,y)
	#렌더링
	update_canvas()
	x += dx*5
	frame = (frame+1)%8
	#frame += 1
	#if frame >= 8: sx = 0

	handle_events()
	delay(0.01)
	#로직

delay(2)
close_canvas()
