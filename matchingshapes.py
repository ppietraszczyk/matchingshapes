#!/usr/bin/python3
import os
os.environ["PYSDL2_DLL_PATH"] = r"."
import sys
from sdl2 import *
from sdl2.sdlimage import *
from sdl2.sdlttf import *
import ctypes
import random
import math
import numpy as np

BLOCK_SIZE=40
MAXRAND=4
FIG=3
SCREEN_WIDTH = 15*BLOCK_SIZE
SCREEN_HEIGHT = 15*BLOCK_SIZE
FPS = 60
FRAME_DELAY = int(1000 / FPS)
X = 1
Y = 2
OX = 3
OY = 4
all = np.zeros((15, 15))


figure=[[[[0,0,0,0],
		[0,0,1,0],
		[0,1,1,0],
		[0,0,1,0]],

		[[0,0,0,0],
		[0,0,1,0],
		[0,1,1,1],
		[0,0,0,0]],

		[[0,0,0,0],
		[0,0,1,0],
		[0,0,1,1],
		[0,0,1,0]],

		[[0,0,0,0],
		[0,0,0,0],
		[0,1,1,1],
		[0,0,1,0]]],



		[[[0,0,1,0],
		[0,0,1,0],
		[0,0,1,0],
		[0,0,1,0]],

		[[0,0,0,0],
		[0,0,0,0],
		[1,1,1,1],
		[0,0,0,0]],

		[[0,0,1,0],
		[0,0,1,0],
		[0,0,1,0],
		[0,0,1,0]],

		[[0,0,0,0],
		[0,0,0,0],
		[1,1,1,1],
		[0,0,0,0]]],



		[[[0,0,1,0],
		[0,0,1,0],
		[0,0,1,0],
		[0,0,1,1]],

		[[0,0,0,0],
		[0,0,0,0],
		[1,1,1,1],
		[1,0,0,0]],

		[[0,1,1,0],
		[0,0,1,0],
		[0,0,1,0],
		[0,0,1,0]],

		[[0,0,0,0],
		[0,0,0,1],
		[1,1,1,1],
		[0,0,0,0]]],



		[[[0,0,0,0],
		[0,0,0,0],
		[0,1,1,0],
		[0,1,1,0]],

		[[0,0,0,0],
		[0,0,0,0],
		[0,1,1,0],
		[0,1,1,0]],

		[[0,0,0,0],
		[0,0,0,0],
		[0,1,1,0],
		[0,1,1,0]],

		[[0,0,0,0],
		[0,0,0,0],
		[0,1,1,0],
		[0,1,1,0]]],



		[[[0,0,1,0],
		[0,0,1,0],
		[0,0,1,0],
		[0,1,1,0]],

		[[0,0,0,0],
		[1,0,0,0],
		[1,1,1,1],
		[0,0,0,0]],

		[[0,0,1,1],
		[0,0,1,0],
		[0,0,1,0],
		[0,0,1,0]],

		[[0,0,0,0],
		[0,0,0,0],
		[1,1,1,1],
		[0,0,0,1]]]]

class Sprite():
	def __init__(self):
		self.cell=[]
		self.x=0
		self.y=0
		#self.bottom=False
		#self.cx=0
		#self.cy=0
		#self.f=0

	def add(self, c):
		global X, Y
		if c != None:
			self.cell.append(c)
			self.x = c[X]
			self.y = c[Y]

	def del_sprite(self):
		if self.cell != None:
			self.cell = []
			self.x = 0
			self.y = 0

	def set_pos(self, x, y, c):
		global X, Y
		#print("self.cell")
		#print(self.cell)
		#print("c")
		#print(c)
		if c != None:
			c[X] = x
			c[Y] = y

	def get_pos(self, c):
		global X, Y
		if c != None:
			return c[X], c[Y]
		else:
			return None, None

	def set_offset(self, x, y, c):
		global OX, OY
		if c != None:
			c[OX] = x
			c[OY] = y

	def get_offset(self, c):
		global OX, OY
		if c != None:
			#print ("_x: %d" % c[OX])
			#print ("_y: %d" % c[OY])
			return c[OX], c[OY]

	def draw(self, renderer, highlight=False):
		# Rysowanie każdego bloku klocka
		for c in self.cell:
			rect = SDL_Rect(c[1], c[2], BLOCK_SIZE, BLOCK_SIZE)
			#rect = SDL_Rect(0,0, BLOCK_SIZE, BLOCK_SIZE)
			#print ("DRAW")
			#print ("c[1]: %d" % c[1])
			#print ("c[2]: %d" % c[2])
			#print(c[0])
			if c[0] == 1:
				#if highlight:
				SDL_SetRenderDrawColor(renderer, 255, 255, 0, 255)  # Żółty klocek
				#else:
				#   SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255)  # Biały klocek
				SDL_RenderFillRect(renderer, ctypes.byref(rect))
				SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255)  # Czarny kontur
				SDL_RenderDrawRect(renderer, ctypes.byref(rect))

		for y in range(15):
			for x in range(15):
				if all[y, x] == 1:
					rect = SDL_Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
					#print("RYSUJE ALL")
					#print("x: %d: " % x)
					#print("y: %d: " % y)
					SDL_SetRenderDrawColor(renderer, 255, 255, 0, 255)  # Żółty klocek
					#else:
					#   SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255)  # Biały klocek
					SDL_RenderFillRect(renderer, ctypes.byref(rect))
					SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255)  # Czarny kontur
					SDL_RenderDrawRect(renderer, ctypes.byref(rect))


	def get_world_blocks(self):
		"""Zwraca pozycje bloków w świecie (z uwagi na x,y)"""

		block = []
		#print("CELL")
		#print(self.cell)
		for c, x, y, ox, oy in self.cell:
			#print ("get_world_blocks")
			#print ("x %d" % x)
			#print ("y %d" % y)
			block.append((x, y))
		#print("POZYCJE BLOKOW  W ŚWIECIE")
		#print (blocks)
		return block

	def add_to_all(self):
		global all
		for c in self.cell:
			#mvx = c[1] % BLOCK_SIZE
			#mvy = c[2] % BLOCK_SIZE
			#vx = (c[1]-mvx)/BLOCK_SIZE
			#vy = (c[2]-mvy)/BLOCK_SIZE
			vx = c[1] / BLOCK_SIZE
			vy = c[2] / BLOCK_SIZE
			tab_x = np.array([vx])
			tab_y = np.array([vy])
			tab_x = tab_x.astype(int)
			tab_y = tab_y.astype(int)
			if c[0] == 1 and vy >= 0 and vx >= 0:
				all[tab_y, tab_x] = 1



def check_adjacency(block1, block2):
	"""Sprawdza czy dwa bloki są przylegające (dotykają się bokami lub rogami)"""
	blocks1 = block1.get_world_blocks()
	for x1, y1 in blocks1:
		for y2 in range(15):
			for x2 in range(15):
				# Sprawdzamy czy bloki są przylegające (różnica nie większa niż rozmiar bloku)
				if block2[y2, x2] == 1:
					dx = abs(x1 - x2 * BLOCK_SIZE)
					dy = abs(y1 - y2 * BLOCK_SIZE)
					# Bloki są przylegające jeśli mają wspólny bok lub róg
					if (dx <= BLOCK_SIZE and dy <= BLOCK_SIZE) and not (dx == 0 and dy == 0):
						print ("CCCCCCCCCCCCC")
						return True
	return False

def is_block_adjacent_to_others(block, other_blocks):
	"""Sprawdza czy blok jest przylegający do któregoś z innych bloków"""
	if check_adjacency(block, other_blocks):
		#other_blocks.append(block)
		print ("AAAAAAAAAAAA")
		return True
	return False


def main():
	# Inicjalizacja SDL
	if SDL_Init(SDL_INIT_VIDEO) < 0:
		print("Nie można zainicjalizować SDL:", SDL_GetError())
		return -1

	# Tworzenie okna
	window = SDL_CreateWindow(b"Block Game",
							 SDL_WINDOWPOS_UNDEFINED,
							 SDL_WINDOWPOS_UNDEFINED,
							 SCREEN_WIDTH, SCREEN_HEIGHT,
							 SDL_WINDOW_SHOWN)
	if not window:
		print("Nie można utworzyć okna:", SDL_GetError())
		SDL_Quit()
		return -1

	# Tworzenie renderera
	renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED)
	if not renderer:
		print("Nie można utworzyć renderera:", SDL_GetError())
		SDL_DestroyWindow(window)
		SDL_Quit()
		return -1

	sprite = Sprite()
	v=random.randint(0,FIG)
	n=random.randint(0,MAXRAND)
	xx = int((SCREEN_WIDTH / 2) - (2 * BLOCK_SIZE))
	yy = int(SCREEN_HEIGHT  - (4 * BLOCK_SIZE))
	for y in range(4):
		for x in range(4):
			sprite.add([np.array(figure[n][v][y][x]),  xx + (x * BLOCK_SIZE), yy + (y * BLOCK_SIZE), 0, 0])

	xx = int((SCREEN_WIDTH / 2) + (2 * BLOCK_SIZE))
	yy = int(SCREEN_HEIGHT  - (10 * BLOCK_SIZE))
	wall = Sprite()
	for y in range(4):
		for x in range(4):
			wall.add([np.array(figure[0][0][y][x]),  xx + (y * BLOCK_SIZE), yy + (x * BLOCK_SIZE), 0, 0])
	wall.add_to_all()

	is_selected = False
	selected_block = None
	offset_x = 0
	offset_y = 0
	running = True
	clock = SDL_GetTicks()


	while running:
		current_time = SDL_GetTicks()

		event = SDL_Event()
		while SDL_PollEvent(ctypes.byref(event)):
			offset = []
			if event.type == SDL_QUIT:
				running = False
			elif event.type == SDL_MOUSEBUTTONDOWN:
				if event.button.button == SDL_BUTTON_LEFT:
					mouse_x, mouse_y = event.button.x, event.button.y
					# Sprawdzamy czy kliknięto na blok na dole

					no_reverse = sprite.get_world_blocks()
					blocks = no_reverse[::-1] # odwracamy
					print(blocks)
					i = 0
					for x, y in blocks:
						#print("BLOCKS")
						#print(blocks)
						if (x <= mouse_x <= x + BLOCK_SIZE and
							y <= mouse_y <= y + BLOCK_SIZE):
							is_selected = True
							selected_block = sprite
							#print(selected_block)
							pole_position_x = 0
							pole_position_y = 0
							for c in selected_block.cell:
								if i >= 4:
									pole_position_x = 0
									pole_position_y += BLOCK_SIZE
									i = 0

								offset_xx = mouse_x - x
								offset_yy = mouse_y - y
								#print ("-___offest_x %d " % offset_xx)
								#print ("-___offset_y %d " % offset_yy)

								offset_x = offset_xx + pole_position_x
								offset_y = offset_yy + pole_position_y
								i += 1
								#print ("-offest_x %d " % offset_x)
								#print ("-offset_y %d " % offset_y)
								#print ("poleposition_x %d" % pole_position_x)
								#print ("poleposition_y %d" % pole_position_y)

								selected_block.set_offset(offset_x, offset_y, c)

								pole_position_x += BLOCK_SIZE

							break
			elif event.type == SDL_MOUSEBUTTONUP:
				if event.button.button == SDL_BUTTON_LEFT and is_selected:
					# Sprawdzamy czy blok jest przylegający do któregoś z innych bloków
					#if selected_block.is_block_adjacent_to_others(all):
					if is_block_adjacent_to_others(selected_block, all):
						# Dodajemy blok do listy wszystkich bloków
						selected_block.add_to_all()
					'''
					ret_block = clear_full_rows(all_blocks, SCREEN_WIDTH, SCREEN_HEIGHT)
						if ret_block != None:
							# Sprawdzamy i usuwamy pełne wiersze
							all_blocks = clear_full_rows(all_blocks, SCREEN_WIDTH, SCREEN_HEIGHT)

						# Tworzymy nowy blok na dole
						bottom_block = create_random_block(
							SCREEN_WIDTH // 2 - BLOCK_SIZE // 2,
							SCREEN_HEIGHT - BLOCK_SIZE * 3
						)
						#print("all_blocks:", all_blocks)
						#print("type(all_blocks):", type(all_blocks))
						# Sprawdzamy kolizje z istniejącymi blokami
						if check_block_collision(bottom_block, all_blocks):
							print("KONIEC GRY")
							exit (1)
                        '
                        while check_block_collision(bottom_block, all_blocks):
                            x = random.randint(0, SCREEN_WIDTH - BLOCK_SIZE)
                            y = random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE)
                            bottom_block = create_random_block(x, y)

					else:
						# Jeśli nie są przylegające, nie dodajemy bloku
						pass
					'''
					sprite.del_sprite()
					v=random.randint(0,FIG)
					n=random.randint(0,MAXRAND)
					xx = int((SCREEN_WIDTH / 2) - (2 * BLOCK_SIZE))
					yy = int(SCREEN_HEIGHT  - (4 * BLOCK_SIZE))
					for y in range(4):
						for x in range(4):
							sprite.add([np.array(figure[n][v][y][x]),  xx + (x * BLOCK_SIZE), yy + (y * BLOCK_SIZE), 0, 0])

					is_selected = False
					selected_block = None

			elif event.type == SDL_MOUSEMOTION and is_selected:
				if selected_block:
					#print ("selectef_block.x %d " % selected_block.x)
					#print ("selected_block.y %d " % selected_block.y)
					mouse_x, mouse_y = event.motion.x, event.motion.y
					for c in selected_block.cell:
						offset_x, offset_y = selected_block.get_offset(c)
						#print ("offset_x: %d" % offset_x)
						#print ("offset_y: %d" % offset_y)
						selected_block.set_pos(mouse_x - offset_x, mouse_y - offset_y, c)
						#print ("selectef_block.x %d " % c[0])
						#print ("selected_block.y %d " % c[1])
		if current_time - clock > 16:
			clock = current_time

			# Wyczyszczenie ekranu
			SDL_SetRenderDrawColor(renderer, 50, 50, 50, 255)
			SDL_RenderClear(renderer)


			#for l in range(len(sprite.cell)):
				#gameDisplay.blit(sprite.cell[l].getSurface(), (sprite.cell[l].getX(), sprite.cell[l].getY()))
			#print(sprite.cell)
			sprite.draw(renderer, highlight=True)

			SDL_RenderPresent(renderer)

if __name__ == "__main__":
	sys.exit(main())
