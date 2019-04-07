#!/usr/bin/python3

import sys,pygame
from algorithms import *

pygame.init()
size = width,height = 990,540

gray  = (50,50,50)

black = (0,0,0)
white = (255,255,255)
blue  = (0,0,255)
green = (0,255,0)
red   = (255,0,0)
c6    = (255,255,0)
c7    = (255,0,255)
c8    = (0,255,255)
c9    = (100,50,50)
c10   = (50,100,50)
c11   = (50,50,100)
c12   = (100,0,100)
c13   = (0,100,100)
c14   = (8,64,255)
c15   = (32,4,128)
c16   = (6,6,6)

screen = pygame.display.set_mode(size)

screen.fill(gray)
pygame.display.flip()

p1 = None

while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONUP:
			ms = pygame.mouse.get_pos()
			if p1 is None :
				p1 = ms
			else :
				ms = pygame.mouse.get_pos()
				ps = mid_point_circle(p1,ms)
				p1 = None
				for i in ps:
					screen.set_at(i,blue)
				pygame.display.flip()

#	ms = pygame.mouse.get_pos()
#	screen.set_at(ms,white)
