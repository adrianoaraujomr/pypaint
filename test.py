#!/usr/bin/python3

import sys,pygame
from algorithms import *

pygame.init()
size = width,height = 990,540

gray  = (50,50,50)

colors = {
pygame.K_q:(0,0,0),
pygame.K_a:(255,255,255),
pygame.K_z:(0,0,255),
pygame.K_w:(0,255,0),
pygame.K_s:(255,0,0),
pygame.K_x:(255,255,0),
pygame.K_e:(255,0,255),
pygame.K_d:(0,255,255),
pygame.K_c:(100,50,50),
pygame.K_r:(50,100,50),
pygame.K_f:(100,0,100),
pygame.K_v:(0,100,100),
pygame.K_t:(8,64,255),
pygame.K_g:(32,4,128),
pygame.K_b:(163,69,115),
pygame.K_y:(232,121,171)
}

screen = pygame.display.set_mode(size)
screen.fill(gray)
pygame.display.flip()

p1 = None
md = 1   #Mode (line(X),circle(X),polyline(X),curve( ),rectangle( ),fill( ))
mc = (255,255,255) #Color

while True:
	for event in pygame.event.get():
		if   event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if   event.key == pygame.K_1:
				md = 1
			elif event.key == pygame.K_2:
				md = 2
			elif event.key == pygame.K_3:
				md = 3
			elif event.key == pygame.K_4:
				md = 4
			elif event.key == pygame.K_5:
				md = 5
			elif event.key == pygame.K_6:
				md = 6
			else:
				mc = colors[event.key]

		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 2:
				p1 = None
				screen.fill(gray)
				pygame.display.flip()
			if p1 is None and event.button == 1:
				ms = pygame.mouse.get_pos()
				if md == 6:
					aux = {}
					wmatrix = pygame.surfarray.array2d(screen)
#					for j in wmatrix:
#						for i in j:
#							if i in aux.keys():
#								aux[i] += 1
#							else:
#								aux[i]  = 1
#					print(aux)
					icolor  = mc[0]*65536 + mc[1]*256 + mc[2]
					ps = flood_field(wmatrix,ms,icolor)
					for i in ps:
						screen.set_at(i,mc)
					pygame.display.flip()
				else:
					p1 = ms
			elif p1 is not None and event.button == 1:
				ms = pygame.mouse.get_pos()

				if   md == 1: #Line
					ps = bresenham(p1,ms)
					p1 = None
				elif md == 2: #Circle
					ps = mid_point_circle(p1,ms)
					p1 = None
				elif md == 3: #Polyline
					ps = bresenham(p1,ms)
					p1 = ms

				for i in ps:
					screen.set_at(i,mc)
				pygame.display.flip()
#				wmatrix = pygame.surfarray.array2d(screen)
#				print(wmatrix[ms[0]][ms[1]])
			elif p1 is not None and event.button == 3:
				p1 = None
