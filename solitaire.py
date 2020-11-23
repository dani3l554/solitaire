"""
Pygame implementation of the game Solitaire.
By Daniel Nicholson. Started 23.11.2020.
"""
import pygame as pg

pg.init()

WIDTH = 1600
HEIGHT = int(round((9/16)*WIDTH,0))

WHITE = (255,255,255)
BLACK = (0,0,0)

display = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Solitaire")
clock = pg.time.Clock()

def exit_game():
    pg.quit()
    exit(0)

def menu():
    in_menu = True
    while in_menu:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit_game()
        display.fill(WHITE)

        pg.display.update()
        clock.tick(15)

menu()

pg.quit()
