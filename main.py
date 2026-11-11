from pygame import * 

DARK_BLUE = (0, 0, 100)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BACK = (200, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

WIN_WIDTH = 700
WIN_HEIGHT = 400

window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = time.Clock()

run = True
while run:
    window.fill(BACK)
    
    for e in event.get():
        if e.type == QUIT:
            run = False  

    clock.tick(30)
    display.update()