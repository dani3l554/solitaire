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

class Text:
	def __init__(self, x, y, text, font, font_size, colour):
		self.x = x
		self.y = y
		self.text = text
		self.font = font
		self.font_size = font_size
		self.colour = colour

	def gen_text_objs(self):
		font_obj = pg.font.Font(self.font, self.font_size)
		text_surface = font_obj.render(self.text, True, self.colour)
		return text_surface, text_surface.get_rect()

	def draw_text(self):
		text_surface, text_rect = self.gen_text_objs()
		text_rect.center = (self.x,self.y)
		display.blit(text_surface,text_rect)

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
