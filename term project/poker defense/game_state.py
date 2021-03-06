import random
from pico2d import *
import gfw
import gobj
from button import Button
import poker_state
stage_x = 10
stage_y = 25
theme = 'ingame'
TEXT_COLOR = (255, 255, 255)
wave = 1
stage = 1
def start(theme):
    pause()
    poker_state.theme = theme
    gfw.push(poker_state)
def enter():
    build_world()
def resume():
    build_world()
def build_world():
    gfw.world.init(['ingame_bg','ingame_ui'])
    center = get_canvas_width()//2, get_canvas_height()//2
    
    global font
    font = gfw.font.load(gobj.res('StarcraftNormal.ttf'), 40)    
    gfw.world.add(gfw.layer.ingame_bg, gobj.ImageObject(theme + '/tile_map.png', center))

    l,b,w,h = 25,550,get_canvas_width()-550,50
    btn = Button(l,b,w,h,font,"poker",lambda: start("poker"))
    gfw.world.add(gfw.layer.ingame_ui, btn)
    l+=250
    btn = Button(l,b,w,h,font,"Ranking",lambda: play())
    gfw.world.add(gfw.layer.ingame_ui, btn)
    l+=250
    btn = Button(l,b,w,h,font,"option",lambda: play())
    gfw.world.add(gfw.layer.ingame_ui, btn)
    b =0
    btn = Button(l,b,w,h,font,"play",lambda:play() )
    gfw.world.add(gfw.layer.ingame_ui, btn)
def play():
    pass
def update():
    gfw.world.update()
def pause():
    pass
def draw():
    global font, stage, wave, window
    gfw.world.draw()
    font.draw(stage_x, stage_y, "STAGE %d"%stage, TEXT_COLOR)
    font.draw(stage_x+250, stage_y, "wave %d"%wave, TEXT_COLOR)
def handle_event(e):
    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            return gfw.pop()
    if handle_mouse(e):
        return
capture = None 
def handle_mouse(e):
    global capture
    if capture is not None:
        holding = capture.handle_event(e)
        if not holding:
            capture = None
        return True

    for obj in gfw.world.objects_at(gfw.layer.ingame_ui):
        if obj.handle_event(e):
            capture = obj
            return True

    return False
def exit():
	pass
if __name__ == '__main__':
    gfw.run_main()