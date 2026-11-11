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

class GameSprite(sprite.Sprite):
    def __init__(self, img_player, x, y, width, height, speed = 10):
        super().__init__()
        self.image = transform.scale(image.load(img_player), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
      
        
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        
        if keys[K_RIGHT] and self.rect.x < 620:
            self.rect.x += self.speed
        if keys[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed

window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = time.Clock()
ball = GameSprite("ball.webp", WIN_WIDTH/2, WIN_HEIGHT/2, 50, 50, 10)


run = True
while run:
    window.fill(BACK)
    ball.reset()
    
    for e in event.get():
        if e.type == QUIT:
            run = False  

    clock.tick(30)
    display.update()