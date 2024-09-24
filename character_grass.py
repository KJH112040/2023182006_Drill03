from pico2d import *

def run_rectangle():
    pass

def run_circle():
    pass

open_canvas()

# fill here
grass = pico2d.load_image('grass')
character = load_image('character.png')


while True:
    run_rectangle()
    run_circle()

close_canvas()
