#!/usr/bin/python3

import sys,pygame
from algorithms import *

pygame.init()
#size = width,height = 320,240
size = width,height = 990,540
#speed = [2,2]

black = (0,0,0)
white = (255,255,255)
gray  = (50,50,50)
blue  = (0,0,255)

screen = pygame.display.set_mode(size)

#ball = pygame.image.load("intro_ball.gif")
#ballrect = ball.get_rect()

#while l:
#	for event in pygame.even.get():
#		if event.type = pygame.QUIT:
#			sys.exit()

#	ballrect = ballrect.move(speed)

#	if ballrect.left < 0 or ballrect.right > width:
#		speed[0] = -speed[0]
#	if ballrect.top  < 0 or ballrect.bottom > height:
#		speed[1] = -speed[1]

#	screen.fill(black)
#	screen.blit(ball,ballrect)
#	pygame.dysplay.flip()

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
				ps = bresenham(p1,ms)
				p1 = None
				for i in ps:
					screen.set_at(i,blue)
				pygame.display.flip()

#	ms = pygame.mouse.get_pos()
#	screen.set_at(ms,white)
