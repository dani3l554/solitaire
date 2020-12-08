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

RED = (220,0,0)
GREEN = (0,220,0)
BLUE = (0,0,220)

BACKGROUND_IMG = pg.image.load("assets/background.png")
TITLE_FONT_DIR = "assets/Anna.ttf"

display = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Solitaire")
clock = pg.time.Clock()

class Text:
	def __init__(self, x: int, y: int, text: str, font: str, font_size: int, colour: tuple):
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

class Button:
	def __init__(self, x: int, y: int, w: int, h: int, ac: tuple, ic: tuple, command = None):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.ic = ic
		self.ac = ac
		self.command = command
		self.text = ""
		self.font = ""
		self.font_size = 0
		self.font_colour = ()
		self._rect = pg.Rect(x,y,w,h)

	def set_text(self, text: str, font: str, font_size: int, font_colour: tuple):
		self.text = text
		self.font = font
		self.font_size = font_size
		self.font_colour = font_colour

	def handle_click(self):
		self.command()

	def draw_button(self):
		if self.is_active():
			pg.draw.rect(display, self.ac, (self.x, self.y, self.w, self.h))
		else:
			pg.draw.rect(display, self.ic, (self.x, self.y, self.w, self.h))

	def is_active(self) -> bool:
		mouse_pos = pg.mouse.get_pos()
		if self._rect.collidepoint(mouse_pos):
			return True
		return False

def exit_game():
	pg.quit()
	exit(0)

def menu():
	in_menu = True
	while in_menu:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				exit_game()
		display.blit(BACKGROUND_IMG, (0,0))
		Text(WIDTH / 2, 150, "Solitaire", TITLE_FONT_DIR, 180, WHITE).draw_text()
		Text(WIDTH / 2, 300, "Created by Daniel Nicholson", TITLE_FONT_DIR, 45, WHITE).draw_text()

		Button(WIDTH/2 - 100, 500, 200, 120, (0,255,0), GREEN, exit_game).draw_button()

		pg.display.update()
		clock.tick(15)

menu()

pg.quit()
