import itertools
import pygame as pg


pg.init()

size = int(input())
amount = int(input())
screen = pg.display.set_mode((size, size))
clock = pg.time.Clock()
width, height = screen.get_size()
block_size = size // amount


background = pg.Surface((width, height))
colors = itertools.cycle((pg.Color('white'), pg.Color('black')))

for y in range(0, height, block_size):
    for x in range(0, width, block_size):
        rect = (x, y, block_size, block_size)
        pg.draw.rect(background, next(colors), rect)
    next(colors)

screen.blit(background, (0, 0))
pg.display.flip()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


