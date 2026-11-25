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
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y < WIN_HEIGHT-self.rect.height:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y < WIN_HEIGHT-self.rect.height:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed

window = display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = time.Clock()
ball = GameSprite("ball.webp", WIN_WIDTH/2, WIN_HEIGHT/2, 50, 50, 10)
platform_left = Player("platform.png", 10, WIN_HEIGHT/2, 39/1.5, 136/1.5, 10)
platform_right = Player("platform.png", 670, WIN_HEIGHT/2, 39/1.5, 136/1.5, 10)

d_x = 3
d_y = -3

run = True
while run:
    window.fill(BACK)
    ball.reset()
    platform_left.reset()
    platform_left.update_l()
    platform_right.reset()
    platform_right.update_r()

    ball.rect.x += d_x
    ball.rect.y += d_y

    if ball.rect.y > WIN_HEIGHT - ball.rect.height:
        d_y *= -1

    if ball.rect.y < 0:
        d_y *= -1

    if sprite.collide_rect(ball, platform_left) or sprite.collide_rect(ball, platform_right):
        d_x *= -1


    for e in event.get():
        if e.type == QUIT:
            run = False  

    clock.tick(30)
    display.update()