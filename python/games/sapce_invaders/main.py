# sapce invaiders game with pygame
# By: angater1 and slime3000fly

import sys
import pygame
import random
from pygame import mixer
from Bullet import Bullet
from enemy import Enemy
from house import House

pygame.init()
pygame.display.init()
fps_controller = pygame.time.Clock()

screen = pygame.display.set_mode((1080, 720))

score = 0

# reading highest score from txt
f = open('highest_score.txt', 'r')
highest_score = int(f.read())
f.close()

x_player = 1080 / 2
y_player = 720
x_bullet = 0

velocity = 3
bullet_velocity = 2

fps = 120

enemy_state = 'RENDER'

wall_left = pygame.Rect(0, 0, 5, 740)
wall_right = pygame.Rect(1075, 0, 10, 740)

# bullets
bullets = [Bullet(screen, 700, 'UP', 10, 10, bullet_velocity), Bullet(screen, 700, 'UP', 10, 10, bullet_velocity)]
bullets_state = ['NORENDER', 'NORENDER']
ticks_to_ignore = 0  # variable to store number of ticks to ignore key reading

playerImg = pygame.image.load('Player.png')
background = pygame.image.load('background.jpg')

# enemies
number_of_enemies = 46
enemies_y = [40, 450, 0]
enemy = [0] * 50
enemy_state = ['RENDER'] * number_of_enemies
enemy_bullet = [Bullet(screen, -100, 'DOWN', 10, 10, bullet_velocity) for i in range(5)]
enemy_bullet_status = ['NORENDER' for i in range(3)]
enemy_direction = 'LEFT'
enemy_x = [0] * number_of_enemies

# creating enemy type object
enemies = [Enemy(screen, i * 50 + 200, 1040, 0) for i in range(15)]
for i in range(number_of_enemies):
    if i > 15 and i <= 30:
        enemies.append(Enemy(screen, (i - 16) * 50 + 200, 1040, 0))
    if i > 30:
        enemies.append(Enemy(screen, (i - 31) * 50 + 200, 1040, 0))

# house
houses_y = 500
houses = [House(screen, houses_y, 900), House(screen, houses_y, 500), House(screen, houses_y, 100)]
houses_health = [4] * 3
hou = [0] * 3

ticku = 0

# sound
mixer.music.set_volume(0.1)
mixer.music.load('Simplicity(by damn so deep).mp3')
mixer.music.play(-1)
bang_sound = mixer.Sound('bang.wav')
score_sound = mixer.Sound('score.wav')
ai_score_sound = mixer.Sound('ai_score.wav')

# color
red = pygame.Color(139, 0, 0)
blue = pygame.Color(51, 255, 255)
white = pygame.Color(255, 255, 255)
orange = (255, 100, 0)
yellow = (255, 50, 170)
green = (34, 177, 76)
black = (0, 0, 0)


# function declaration
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('  Player: ' + str(score) + '  Highest Score : ' + str(highest_score), True, color)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)

def lose():
    # function which play after lose game
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.QUIT: sys.exit()
        # drawing writing 'you lose'
        font = pygame.font.Font('freesansbold.ttf', 52)
        text = font.render('YOU LOSE', True, red, black)
        # text surface object
        textRect = text.get_rect()
        # set the center of the rectangular object.
        textRect.center = (540, 360)
        screen.blit(text, textRect)
        pygame.display.update()


def won():
    # function which play after lose game
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.QUIT: sys.exit()
        # drawing writing 'you lose'
        font = pygame.font.Font('freesansbold.ttf', 52)
        text = font.render('YOU WON', True, green, black)
        # text surface object
        textRect = text.get_rect()
        # set the center of the rectangular object.
        textRect.center = (540, 360)
        screen.blit(text, textRect)
        pygame.display.update()


value = [0, 0, 0]
trash = [0, 0, 0]


def render_enemy_bullet():
    for i in range(number_of_enemies - 1):
        if enemy_state.count('RENDER') > 3:
            if enemies[i].return_if_x_is_max():
                for z in range(3):
                    value[z] = random.randrange(44)
                    if value[z] in value:
                        value[z] = random.randrange(44)

                for o in range(3):
                    trash[o] = enemy_state[value[o]]

                while True:
                    if 'NORENDER' in trash:
                        guu = trash.index('NORENDER')
                        value[guu] = random.randrange(44)
                        trash[guu] = enemy_state[value[guu]]
                    else:
                        break
        else:
            value[0] = enemy_state.index('RENDER')

    for i in range(45):
        if enemies[i].return_if_x_is_max():
            for d in range(3):
                enemy_bullet_status[d] = 'RENDER'
    for z in range(3):
        print('value',value[z])
        print('len',len(enemies))
        print(enemies[value[z]].return_current_x())
        enemy_bullet[z].draw(enemies[value[z]].return_current_x(), enemies_y[2], enemy_bullet_status[z])


done = False

while not done:
    # key to control
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        if x_player > 0 + 15:
            x_player -= velocity
    if pressed[pygame.K_RIGHT]:
        if x_player < 1080 - 15:
            x_player += velocity
    if pressed[pygame.K_ESCAPE]:
        done = True
    if pressed[pygame.K_SPACE]:
        for i in range(0, 2):
            if (bullets_state[i] == 'NORENDER' and ticks_to_ignore == 0):
                bullets_state[i] = 'RENDER'
                ticks_to_ignore = 20
                x_bullet = x_player
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # drawing elements
    pygame.draw.rect(screen, red, wall_right)
    pygame.draw.rect(screen, red, wall_left)
    enemy_rect = pygame.Rect(1080 / 2, 720 / 2, 10, 20)
    player_rect = pygame.Rect(x_player, y_player, 15, 30)
    player_rect.center = (x_player, 700)
    # pygame.draw.rect(screen, white, player_rect)
    screen.blit(playerImg, (x_player-7.5, 680))

    # drawing player's bullet and check colision with enemies and houses
    for i in range(0, 2):
        bullets[i].draw(x_bullet, 680, bullets_state[i])
        if (bullets_state[i] == 'RENDER'):
            for b in range(0, 3):
                if houses_health[b] > 0:
                    if pygame.Rect.colliderect(hou[b], bullets[i].check_colison()):
                        bullets_state[i] = 'NORENDER'
                        houses_health[b] -= 1
                        ticks_to_ignore += 5
            for b in range(0, number_of_enemies - 1):
                if enemy_state[b] == 'RENDER':
                    if pygame.Rect.colliderect(bullets[i].check_colison(), enemy[b]):
                        enemy_state[b] = 'NORENDER'
                        bullets_state[i] = 'NORENDER'
                        score +=1

        if (bullets[i].returnY() <= -1): bullets_state[i] = 'NORENDER'

    # drawing houses
    for i in range(0, 3):
        hou[i] = houses[i].draw(houses_health[i])

    # drawing enemies
    for i in range(0, number_of_enemies - 1):
        if i < 15: c = 0
        if i >= 15 and i < 30: c = 1
        if i >= 30 and i <= 46: c = 2
        enemy[i] = enemies[i].draw(enemy_state[i], enemy_direction, enemies_y[c], enemy_x[i])
        if enemies[i].return_current_x() <= 20:
            enemy_direction = 'RIGHT'
            enemies_y[0] += 15
        if enemies[i].return_current_x() >= 1040:
            enemy_direction = 'LEFT'
            enemies_y[0] += 15
    enemies_y[1] = enemies_y[0] + 50
    enemies_y[2] = enemies_y[1] + 50

    # drawing enemies bullet
    render_enemy_bullet()

    # check if plyer lose
    for i in range(0, 3):
        if pygame.Rect.colliderect(enemy_bullet[i].check_colison(), player_rect): lose()
        if enemy_bullet_status[i] == 'RENDER':
            for d in range(3):
                if houses_health[d] > 0:
                    if pygame.Rect.colliderect(enemy_bullet[i].check_colison(), hou[d]):
                        houses_health[d] -= 1
                        print(houses_health[d])
                        enemy_bullet_status[i] = 'NORENDER'
    if enemies_y[1] >= 620: lose()

    # drawing score
    show_score(1, white, 'times new roman', 20)
    pygame.display.flip()
    screen.fill(black)
    screen.blit(background,(0,0))

    if (ticks_to_ignore > 0): ticks_to_ignore -= 1

    if (ticku >= 0): ticku -= 1

    # saving highest score to highest_score.txt
    f = open('highest_score.txt', 'w')
    f.write(str(highest_score))
    f.close()

    # FPS !!!!!
    fps_controller.tick(fps)
#guwno
#zjedz jerowno
#masznatwarzyiciepaczymordo
#guwnooooooooo
#twoja stara = oktylion kg