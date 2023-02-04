from pygame import *



back = (106,90,205) #цвет фона (background)

win_width = 600
win_height = 500

window = display.set_mode((win_width, win_height))

window.fill(back)


game = True


FPS = 60
finish = False
clock = time.Clock()

display.set_caption('Pin-Pong')

while game:
    display.update()
    clock.tick(FPS)
    
    for e in event.get():
        if e.type == QUIT: 
            game = False
    





