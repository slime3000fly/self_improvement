# class for enemy
# method draw enemies and make it move up

import pygame
from Bullet import Bullet


class Enemy:
    x = 1080 / 2
    b = 0
    # color
    green = (0, 255, 0)

    def __init__(self, screen, x_enemy, max_x, min_x, width=20, lenght=20, enemy_velocity=1):
        self.screen = screen
        self.x = x_enemy
        self.width = width
        self.lenght = lenght
        self.enemy_velocity = enemy_velocity
        self.max_x = max_x
        self.min_x = min_x
        self.img = pygame.image.load('Enemy.png')

    def return_if_x_is_max(self):
        return self.x == self.max_x

    def return_current_x(self) -> object:
        return self.x

    def draw(self, render='RENDER', direction='LEFT', y=400,x=200):
        # function to draw, it return enemy which is pygame.rect to colision check
        # establish direction for enemy and bullet status
        if (render == 'RENDER'):
            # drawing enemy
            self.enemy = pygame.Rect(self.x, y, self.width, self.lenght)
            self.screen.blit(self.img,(self.x,y))

            # calucalte x for enemy
            if (direction == 'RIGHT'): self.x += self.enemy_velocity
            if (direction == 'LEFT'): self.x -= self.enemy_velocity

        return self.enemy
