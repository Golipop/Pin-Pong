from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, speed, x, y, w , h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 620:
            self.rect.x += self.speed

main_win = display.set_mode((700, 500))
bg = transform.scale(image.load('fon.png'), (700, 500))

game = True
finish = False

clock = time.Clock()
FPS = 70

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        main_win.blit(bg, (0, 0))
        display.update()
        clock.tick(FPS)
