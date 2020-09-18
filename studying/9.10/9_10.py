from pico2d import *

open_canvas()
img = load_image('../resource/run_animation.png')
gra = load_image('../resource/grass.png')


frame = 0
for x in range(0,800,2):
	clear_canvas()

	gra.draw(400,30)
	img.clip_draw(frame*100,0,100,100,x,80)
	#렌더링
	update_canvas()

	frame = (frame+1)%8
	#frame += 1
	#if frame >= 8: sx = 0

	get_events()
	delay(0.01)
	#로직

delay(2)
close_canvas()
