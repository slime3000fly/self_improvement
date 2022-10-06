# class for generate cells

import pygame


class Cell:
    pos = [0,0]

    def __init__(self, pos):
        self.pos = pos
        self.cell = pygame.Rect(self.pos, (40, 40))


    def draw(self, screen, render='NOREDNER'):
        red = pygame.Color(139, 0, 0)



        if render == 'RENDER':
            pygame.draw.rect(screen, red, self.cell)

    def position(self):
        return self.pos

    def rect(self):
        return self.cell
