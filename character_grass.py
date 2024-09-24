from pico2d import *

def run_rectangle():
    print('RECTANGLE')
    pass

def run_circle():
    print('CIRCLE')
    pass

open_canvas()

# fill here
grass = pico2d.load_image('grass.png')
character = load_image('character.png')


while True:
    run_rectangle()
    run_circle()

close_canvas()
