# The game of life
# by slime3000fly

import asyncio
import copy
import sys
from math import floor

import pygame

from cell import Cell

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((1080, 720))

# number of column and row depend of resolutions
column = int(720 / 40)
row = int(1080 / 40)

cells_render = [['NORENDER'] * int(720 / 40) for _ in range(int(1080 / 40))]
next_cells_render = copy.deepcopy(cells_render)

start_life = False

# creating list of Cell object
cells = [[i] * column for i in range(row)]
for i in range(row):
    for z in range(column):
        pos = [i * 40, z * 40]
        # noinspection PyTypeChecker
        cells[i][z] = Cell(pos)

# color
grey = pygame.Color(220, 220, 220)
dimgray = pygame.Color(105, 105, 105)


def check_neighbors(x, y):
    how_manny_neighbors = 0
    for i in range(-1, 2):
        for z in range(-1, 2):
            # print(i,z)
            if i == 0 and z == 0:
                continue
            if x + i >= row or y + z >= column:
                break
            if x + i < 0 or y + z < 0:
                continue
            if cells_render[x + i][y + z] == 'RENDER':
                how_manny_neighbors += 1

    return how_manny_neighbors


async def life_sterring():
    # function to control program during symulations
    global start_life

    while start_life:
        # key to control
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_life = False
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        drawing_cell()
        await asyncio.sleep(0.0001)


async def is_cell_alive():
    # function to check if in the nex round cell is alvie
    global next_cells_render
    global cells_render

    while start_life:
        await asyncio.sleep(1)
        for i in range(row):
            for o in range(column):
                cells[i][o].draw(screen, cells_render[i][o])

        for i in range(row):
            for z in range(column):
                neighbors = check_neighbors(i, z)
                if cells_render[i][z] == 'RENDER':
                    if neighbors <= 1:
                        next_cells_render[i][z] = 'NORENDER'
                    elif neighbors >= 4:
                        next_cells_render[i][z] = 'NORENDER'
                    else:
                        next_cells_render[i][z] = 'RENDER'
                else:
                    if neighbors == 3:
                        next_cells_render[i][z] = 'RENDER'

        cells_render = copy.deepcopy(next_cells_render)
        pygame.display.flip()


def find_cell(pos):
    found_cell = [0, 0]
    found_cell[0] = floor(pos[0] / 40)  # calculate x for cell
    found_cell[1] = floor(pos[1] / 40)  # calculate y for cell
    return found_cell


def drawing_cell():
    # drawing cells and net
    counter = 0
    for i in range(row):
        for o in range(column):
            cells[i][o].draw(screen, cells_render[i][o])
            if cells_render[i][o] == 'RENDER':
                counter += 1

    # drawing net
    net = 0

    while net <= 1080:
        pygame.draw.line(screen, dimgray, [net, 0], [net, 720], 5)
        pygame.draw.line(screen, dimgray, [0, net], [1080, net], 5)
        net += 40

    pygame.display.flip()
    screen.fill(grey)


def game():
    # main funciotn for run game
    run_game = True
    while run_game:

        # key to control
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_ESCAPE]:
            run_game = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # running 2 funcion in the same time
                    global start_life
                    start_life = True
                    loop = asyncio.get_event_loop()
                    loop.run_until_complete(asyncio.gather(is_cell_alive(), life_sterring()))
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                temp_cell = pygame.Rect(pos, (40, 40))
                cell_number = find_cell(pos)
                if cells_render[cell_number[0]][cell_number[1]] == 'RENDER':
                    if pygame.Rect.colliderect(temp_cell, cells[cell_number[0]][cell_number[1]].rect()):
                        cells_render[cell_number[0]][cell_number[1]] = 'NORENDER'
                else:
                    cells_render[cell_number[0]][cell_number[1]] = 'RENDER'

        drawing_cell()


if __name__ == '__main__':
    game()
