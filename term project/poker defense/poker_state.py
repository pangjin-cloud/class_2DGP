import random
from pico2d import *
import gfw
import gobj
from button import Button
import game_state
from card import Card
import check_hands

theme = 'poker'
TEXT_COLOR = (255, 255, 255)

def start(theme):
	game_state.theme = theme
	gfw.push(game_state)

def enter():
    build_world()
def resume():
    build_world()
def build_world():
    gfw.world.init(['poker_bg','ingame_ui','card'])
    center = get_canvas_width()//2, get_canvas_height()//2
    gfw.world.add(gfw.layer.poker_bg, gobj.ImageObject(theme + '/board.png', center))
    
    global font
    font = gfw.font.load(gobj.res('StarcraftNormal.ttf'), 40)      
    l,b,w,h = 25,550,get_canvas_width()-550,50
    btn = Button(l,b,w,h,font,"ingame",lambda: start("ingame"))
    gfw.world.add(gfw.layer.ingame_ui, btn)
    x,y = 100,100
    global c
    shape = ['Club','Diamond','Heart','spade']
    index = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    c1 = [random.choice(index)]
    c2 = [random.choice(shape)]
    for i in range(0,5):
        c = Card(c1[i],(x,y),c2[i],theme)
        gfw.world.add(gfw.layer.card, c)
        nc1 = random.choice(index)
        nc2 = random.choice(shape)
        c1.append(nc1)
        c2.append(nc2)
        x+=150
    rank = check_hands.hands(c1,c2)
    print(rank)
def update():
    gfw.world.update()

def draw():
	gfw.world.draw()
def handle_event(e):
    if handle_mouse(e):
        return
    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            return gfw.pop()
    global last_card
    for card in gfw.world.objects_at(gfw.layer.card):
        card.handle_event(e)
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
def pause():
    pass
def exit():
	pass

if __name__ == '__main__':
    gfw.run_main()