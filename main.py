from random import randint
from pygame import *
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("pngtree-beautiful-forest-background-image_2120959.jpg"), (win_width, win_height))
game = True
clock = time.Clock()
FPS = 60
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (55,55))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    def reset2(self):
        window.blit(self.image, (-100, -100))
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 3:
            self.rect.x -= self.speed
        if keys [K_RIGHT] and self.rect.x < win_width - 70:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 3:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 70:
            self.rect.y += self.speed
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 350:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
# class Enemy(GameSprite):
#     def update(self):
#         self.rect.y += self.speed
#         global lost
#         if self.rect.y > win_height:
#             self.rect.x = randint(80, win_width - 80)
#             self.rect.y = -50
#             lost += 1
class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.wall_width = wall_width
        self.wall_height = wall_height
        self.image = Surface((self.wall_width, self.wall_height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
happy1 = Wall(154, 205, 50, 0, 0, 800, 10)
happy2 = Wall(154, 205, 50, 0, 10, 10, 600)
happy3 = Wall(154, 205, 50, 690, 10, 10, 500)
happy4 = Wall(154, 205, 50, 200, 490, 500, 10)
happy5 = Wall(154, 205, 50, 0, 375, 205, 10)
happy6 = Wall(154, 205, 50, 200, 90, 10, 200)
happy7 = Wall(154, 205, 50, 0, 280, 100, 10)
happy8 = Wall(154, 205, 50, 340, 376, 170, 10)
happy9 = Wall(154, 205, 50, 590, 0, 10, 280)
happy10 = Wall(154, 205, 50, 340, 280, 10, 100)
happy11 = Wall(154, 205, 50, 200, 280, 150, 10)
happy12 = Wall(154, 205, 50, 340, 375, 10, 150)
happy13 = Wall(154, 205, 50, 590, 335, 10, 50)
happy14 = Wall(154, 205, 50, 340, 270, 175, 10)
happy15 = Wall(154, 205, 50, 510, 90, 10, 190)
happy16 = Wall(154, 205, 50, 390, 90, 125, 10)
happy17 = Wall(154, 205, 50, 200, 90, 125, 10)
happy18 = Wall(154, 205, 50, 100, 200, 100, 10)
happy19 = Wall(154, 205, 50, 100, 90, 10, 120)
player = Player("images-6jdu4LOkj-transformed.png", 60, win_height - 80, 4)
coin_x = 30

coins = []
coin = GameSprite("1_hryvnia_coin_of_Ukraine__2018__averse_-removebg-preview.png", coin_x, win_height - 200, 4)

coin2 = GameSprite("1_hryvnia_coin_of_Ukraine__2018__averse_-removebg-preview.png", 125, win_height - 375, 4)
coin3 = GameSprite("1_hryvnia_coin_of_Ukraine__2018__averse_-removebg-preview.png", 525, win_height - 480, 4)
coin4 = GameSprite("1_hryvnia_coin_of_Ukraine__2018__averse_-removebg-preview.png", 620, win_height - 480, 4)
coin5 = GameSprite("1_hryvnia_coin_of_Ukraine__2018__averse_-removebg-preview.png", 400, win_height - 90, 4)

coins.append(coin)
coins.append(coin2)
coins.append(coin3)
coins.append(coin4)
coins.append(coin5)

monster = Enemy("Ð_ÐµÐ·_Ð½Ð°Ð·Ð²Ð°Ð½Ð¸Ñ_-igcIeoAat-transformed.png", win_width - 80, 280, 3)
goal = GameSprite('images.jpg', 330, 175, 0)
mixer.init()
mixer.music.load("bdd6ff5ec5a8e214 (1).mp3")
mixer.music.play()
font.init()
font1 = font.Font(None, 70)
win = font1.render("YOU WIN!", True, (255, 215, 0))
lose = font1.render("YOU LOSE!", True, (255, 0, 0))
finish = False
score = 0
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        player.update()
        monster.update()
        goal.reset()
        player.reset()
        monster.reset()
        # coins.reset()

        # if not sprite.collide_rect(player, coin) :
        #     coin.reset()
        #     coin2.reset()
        #     coin3.reset()
        #     coin4.reset()
        #     coin5.reset()
        # elif sprite.collide_rect(player, coin):
        #     coin.reset2()
        #     score+=1
        #     if not sprite.collide_rect(player, coin2):
        #         coin2.reset()
        #     elif sprite.collide_rect(player, coin2) and score == 1:
        #         coin2.reset2()
        #         score+=1
        #         if not sprite.collide_rect(player, coin3) and score == 2:
        #             coin3.reset()
        #         elif sprite.collide_rect(player, coin3):
        #             coin3.reset2()
        #             score+=1
        coin.reset()
        coin2.reset()
        coin3.reset()
        coin4.reset()
        coin5.reset()
        happy1.draw_wall()
        happy2.draw_wall()
        happy3.draw_wall()
        happy4.draw_wall()
        happy5.draw_wall()
        happy6.draw_wall()
        happy7.draw_wall()
        happy8.draw_wall()
        happy9.draw_wall()
        happy10.draw_wall()
        happy11.draw_wall()
        happy12.draw_wall()
        happy13.draw_wall()
        happy14.draw_wall()
        happy15.draw_wall()
        happy16.draw_wall()
        happy17.draw_wall()
        happy18.draw_wall()
        happy19.draw_wall()
        # coins.draw(window)
        if player.rect.colliderect(coin.rect):
            coins.remove(coin)

            # coin = GameSprite("1_hryvnia_coin_of_Ukraine__2018__averse_-removebg-preview.png", -400, win_height - 200, 4)
            # coin_x = 400
            # sprite.spritecollide(player, coin, True)

        if sprite.collide_rect(player, goal) :
            finish = True
            window.blit(win, (200, 200))
        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, happy1) or sprite.collide_rect(player, happy2) or sprite.collide_rect(player, happy3) or sprite.collide_rect(player, happy4) or sprite.collide_rect(player, happy5) or sprite.collide_rect(player, happy6) or sprite.collide_rect(player, happy7) or sprite.collide_rect(player, happy8) or sprite.collide_rect(player, happy9) or sprite.collide_rect(player, happy10) or sprite.collide_rect(player, happy11) or sprite.collide_rect(player, happy12) or sprite.collide_rect(player, happy13) or sprite.collide_rect(player, happy14) or sprite.collide_rect(player, happy15) or sprite.collide_rect(player, happy16) or sprite.collide_rect(player, happy17) or sprite.collide_rect(player, happy18) or sprite.collide_rect(player, happy19):
            finish = True
            window.blit(lose, (200, 200))

            # coin.reset()
            # coin.kill()
            # finish = True
           # sprite.spritecollide(player, coin, True)
    else:
        time.delay(3000)
        finish = False
        player = Player("images-6jdu4LOkj-transformed.png", 60, win_height-80, 4)
    display.update()
    clock.tick(FPS)
