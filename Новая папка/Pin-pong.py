from pygame import *



back = (106,90,205) #цвет фона (background)

win_width = 600
win_height = 500

speed_x = 3 
speed_y = 3



window = display.set_mode((win_width, win_height))

window.fill(back)


game = True


FPS = 60
finish = False
clock = time.Clock()

display.set_caption('Pin-Pong')


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y < win_height - 80: 
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y < win_height - 80: 
            self.rect.y += self.speed








ball = GameSprite('ball.png', 250, 200, 3, 100, 50)
racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 500, 200, 4, 50, 150)

while game:
    display.update()
    clock.tick(FPS)
    
    for e in event.get():
        if e.type == QUIT: 
            game = False
    

    ball.update()
    ball.reset()

    racket1.update()
    racket1.reset()

    racket2.update()
    racket2.reset()

    racket1.update_l()
    racket2.update_r()





