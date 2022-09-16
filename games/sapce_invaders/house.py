# class for drawing houses which can be destory


import pygame
from Bullet import Bullet


class House:

    #color
    pink = (204, 0, 204)

    def __init__(self, screen, y_house, x_house, width=150, lenght=50):
        self.screen = screen
        self.y = y_house
        self.x = x_house
        self.width = width
        self.lenght = lenght
        self.img = pygame.image.load('House.png')


    def draw(self,health ,render='RENDER'):
        # function to draw
        if health <= 0: render = 'NORENDER'
        if (render == 'RENDER'):
            #drawing house
            self.house = pygame.Rect(self.x, self.y, self.width, self.lenght)
            self.screen.blit(self.img,(self.x,self.y))

        return self.house

