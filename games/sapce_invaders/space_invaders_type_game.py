# pong game with pygame
# By: angater1 and slime3000fly

import pygame, sys, time, random
from pygame import mixer

pygame.init()
pygame.display.init()
fps_controller = pygame.time.Clock()

screen = pygame.display.set_mode((1080, 720))

# score
score = 0
ai_score = 0

# reading highest score from txt
f = open('highest_score.txt', 'r')
highest_score = int(f.read())
f.close()

# color
black = (0, 0, 0)

initial_x_player = 1060
initial_y_player = 360
initial_x_player_2 = 5
initial_y_player_2 = 360

x_player = 1080 / 2
y_player = 720

x_player_2 = 5
y_player_2 = 360

velocity = 5
bullet_velocity = 30

initial_x_bullet = 530
initial_y_bullet = 355

bullet = [0] * 10
bullet_number = 0

x_bullet = 530
y_bullet = 355
bullet_direction = 'UP'
change_to = bullet_direction
bullet_state = 'NOT_RENDER'
change_bullet_state_to = bullet_state

wall_left = pygame.Rect(0, 0, 5, 740)
wall_right = pygame.Rect(1075, 0, 10, 740)

# sound
mixer.music.set_volume(0.1)
mixer.music.load('Simplicity(by damn so deep).mp3')
mixer.music.play(-1)
bang_sound = mixer.Sound('bang.wav')
score_sound = mixer.Sound('score.wav')
ai_score_sound = mixer.Sound('ai_score.wav')


# function declaration
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(
        'AI: ' + str(ai_score) + '  Player: ' + str(score) + '  Highest Score : ' + str(highest_score), True, color)
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


# color
red = pygame.Color(139, 0, 0)
blue = pygame.Color(51, 255, 255)
white = pygame.Color(255, 255, 255)
orange = (255, 100, 0)
yellow = (255, 50, 170)
green = (34, 177, 76)

done = False

while not done:
    for event in pygame.event.get():

        # key to control
        if event.type == pygame.KEYDOWN:
            pygame.key.set_repeat(10)
            if event.key == pygame.K_LEFT:
                if x_player > 0 + 15:
                    x_player -= velocity
            if event.key == pygame.K_RIGHT:
                if x_player < 1080 - 15:
                    x_player += velocity
            if y_bullet < 0:
                if event.key == pygame.K_SPACE:
                    bullet_state = 'RENDER'
                    x_bullet = x_player - 5
                    y_bullet = y_player - 40
            if event.key == pygame.K_ESCAPE:
                done = True
        if event.type == pygame.QUIT: sys.exit()

    # drawing elements
    pygame.draw.rect(screen, red, wall_right)
    pygame.draw.rect(screen, red, wall_left)
    player_rect = pygame.Rect(x_player, y_player, 20, 30)
    player_rect.center = (x_player, 700)
    pygame.draw.rect(screen, white, player_rect)

    # drawing score
    show_score(1, white, 'times new roman', 20)
    pygame.display.flip()
    screen.fill(black)
    # collisions

    # Moving the bullet
    if bullet_state == 'RENDER':
        bullet = pygame.draw.rect(screen, red, pygame.Rect(x_bullet, y_bullet, 10, 10))

    if bullet_direction == 'UP':
        y_bullet -= bullet_velocity
    if bullet_direction == 'UP_RIGHT':
        x_bullet += bullet_velocity
        y_bullet -= bullet_velocity
    if bullet_direction == 'UP_LEFT':
        x_bullet -= bullet_velocity
        y_bullet -= bullet_velocity

    if ai_score >= score + 5:
        lose()
    if score >= ai_score + 5:
        won()

    # saving highest score to highest_score.txt
    f = open('highest_score.txt', 'w')
    f.write(str(highest_score))
    f.close()

    # FPS !!!!!
    fps_controller.tick(60)
