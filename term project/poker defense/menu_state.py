from pico2d import *
import gobj
import gfw
from button import Button
import game_state

def start(theme):
    if theme == "quit":
        return gfw.quit()
    game_state.theme = theme
    gfw.push(game_state)

def build_world():
    gfw.world.init(['mainmenu_bg','ui'])
    center = get_canvas_width()//2, get_canvas_height()//2
    mainmenu_bg=gobj.ImageObject('main_menu.png',center)

    gfw.world.add(gfw.layer.mainmenu_bg,mainmenu_bg)

    font = gfw.font.load(gobj.res('StarcraftNormal.ttf'), 40)

    l,b,w,h = 25,100,get_canvas_width()-550,80
    btn = Button(l,b,w,h,font,"Start",lambda: start("ingame"))
    gfw.world.add(gfw.layer.ui, btn)
    l+=250
    btn = Button(l,b,w,h,font,"Ranking",lambda: start("ranking"))
    gfw.world.add(gfw.layer.ui, btn)
    l+=250
    btn = Button(l,b,w,h,font,"Quit",lambda: start("quit"))
    gfw.world.add(gfw.layer.ui, btn)

def enter():
    build_world()

def update():
	gfw.world.update()

def draw():
	gfw.world.draw()

capture = None 
def handle_mouse(e):
    global capture
    if capture is not None:
        holding = capture.handle_event(e)
        if not holding:
            capture = None
        return True

    for obj in gfw.world.objects_at(gfw.layer.ui):
        if obj.handle_event(e):
            capture = obj
            return True

    return False

def handle_event(e):
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        return gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            return gfw.pop()

    # print('ms.he()', e.type, e)
    if handle_mouse(e):
        return
def pause():
    pass
def resume():
    build_world()

def exit():
    print("menu_state exits")

if __name__ == '__main__':
	gfw.run_main()
	

