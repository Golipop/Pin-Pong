from pygame import *

font.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, speed, x, y, w , h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed
    def update_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

main_win = display.set_mode((700, 500))
bg = transform.scale(image.load('fon_111.jpg'), (700, 500))

game = True
finish = False

clock = time.Clock()
FPS = 70

Raket_1 = Player('санстрайк.jpg', 5, 670, 0, 30, 100)
Raket_2 = Player('санстрайк.jpg', 5, 0, 0, 30, 100)

Mch = GameSprite('monetka.jpg', 2, 320, 210, 40, 40)

font1 = font.SysFont('Times New Roman', 36)

text_lose1 = font1.render('Игрок 1 проиграл!', 1, (255, 255, 255))
text_lose2 = font1.render('Игрок 2 проиграл!', 1, (255, 255, 255))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        Mch.rect.x += speed_x
        Mch.rect.y += speed_y
        if Mch.rect.y < 0 or Mch.rect.y > 460:
            speed_y *= -1
        if sprite.collide_rect(Raket_1, Mch) or sprite.collide_rect(Raket_2, Mch):
            speed_x *= -1
        if Mch.rect.x < -40:
            finish = True
            bg.blit(text_lose1,(200,200))
        if Mch.rect.x > 740:
            finish = True
            bg.blit(text_lose2,(200,200))
        main_win.blit(bg, (0, 0))
        Raket_1.update_2()
        Raket_1.reset()
        Raket_2.update_1()
        Raket_2.reset()
        Mch.reset()
        display.update()
        clock.tick(FPS)
