#!/usr/bin/python3

import sys,pygame
from algorithms import *

#Global variables-------------------------------------------------------------------------------------
world = {}
size = width,height = 1001,540
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
pl = []
p1 = None
md = 1   #Mode (line(X),circle(X),polyline(X),curve(X),rectangle(X),fill(X))
mc = (255,255,255) #Color

#Functions -------------------------------------------------------------------------------------------
def handle_click(p1,ms,md,mc,pl,ebt):

	if ms[0] >= 900:
		if   ms[0] <= 925  and ms[1] <=  25:
			mc = colors[pygame.K_q]
		elif ms[0] <= 950  and ms[1] <=  25:
			mc = colors[pygame.K_a]
		elif ms[0] <= 975  and ms[1] <=  25:
			mc = colors[pygame.K_z]
		elif ms[0] <= 1000 and ms[1] <=  25:
			mc = colors[pygame.K_w]
		elif ms[0] <= 925  and ms[1] <=  50:
			mc = colors[pygame.K_s]
		elif ms[0] <= 950  and ms[1] <=  50:
			mc = colors[pygame.K_x]
		elif ms[0] <= 975  and ms[1] <=  50:
			mc = colors[pygame.K_e]
		elif ms[0] <= 1000 and ms[1] <=  50:
			mc = colors[pygame.K_d]
		elif ms[0] <= 925  and ms[1] <=  75:
			mc = colors[pygame.K_c]
		elif ms[0] <= 950  and ms[1] <=  75:
			mc = colors[pygame.K_r]
		elif ms[0] <= 975  and ms[1] <=  75:
			mc = colors[pygame.K_f]
		elif ms[0] <= 1000 and ms[1] <=  75:
			mc = colors[pygame.K_v]
		elif ms[0] <= 925  and ms[1] <= 100:
			mc = colors[pygame.K_t]
		elif ms[0] <= 950  and ms[1] <= 100:
			mc = colors[pygame.K_g]
		elif ms[0] <= 975  and ms[1] <= 100:
			mc = colors[pygame.K_b]
		elif ms[0] <= 1000 and ms[1] <= 100:
			mc = colors[pygame.K_y]
		elif ms[1] <= 150:
			md = 1
		elif ms[1] <= 200:
			md = 2
		elif ms[1] <= 250:
			md = 3
		elif ms[1] <= 300:
			md = 4
		elif ms[1] <= 350:
			md = 5
		elif ms[1] <= 400:
			md = 6
		if p1 is not None:
			p1 = None
	elif md == 3 and ebt == 3:
		p1 = None
	elif md == 6:
		aux = {}
		wmatrix = pygame.surfarray.array2d(screen)
		icolor  = mc[0]*65536 + mc[1]*256 + mc[2]
		ps = flood_field(wmatrix,ms,icolor)
		for i in ps:
			world[i] = mc
	elif p1 is None:
		p1 = ms
	else:
		if   md == 1:
			ps = bresenham(p1,ms)
			for i in ps:
				world[i] = mc
			p1 = None
		elif md == 2:
			ps = mid_point_circle(p1,ms)
			for i in ps:
				world[i] = mc
			p1 = None			
		elif md == 3:
			ps = bresenham(p1,ms)
			for i in ps:
				world[i] = mc
			p1 = ms			
		elif md == 4:
			if len(pl) == 0:
				pl.append(p1)
				pl.append(ms)
			elif len(pl) < 3:
				pl.append(ms)
			else:
				pl.append(ms)
				ps = bezier(pl[0],pl[1],pl[2],pl[3])
				for i in ps:
					world[i] = mc
				p1 = None
				pl = []
		elif md == 5:
			ps = rectangle(p1,ms)
			for i in ps:
				world[i] = mc
			p1 = None

	
	aux = []
	aux.append(p1)
	aux.append(md)
	aux.append(mc)
	aux.append(pl)
	return aux



#Menu-------------------------------------------------------------------------------------------------
for i in range(900,1001,1):
	c = 300
	for j in range(0,541):
		if j % 25 == 0 and j <= 100:
			world[(i,j)] = (200,200,200)
		elif j % 25 == 1 and j <= 100:
			world[(i,j)] = (150,150,150)
		elif j % 25 == 2 and j <= 100:
			world[(i,j)] = (100,100,100)
		elif j <= 25:
			if i % 25 == 0:
				world[(i,j)] = (200,200,200)
			elif i < 925:
				world[(i,j)] = colors[pygame.K_q]
			elif i < 950:
				world[(i,j)] = colors[pygame.K_a]
			elif i < 975:
				world[(i,j)] = colors[pygame.K_z]
			else:
				world[(i,j)] = colors[pygame.K_w]
		elif j <= 50:
			if i % 25 == 0:
				world[(i,j)] = (200,200,200)
			elif i < 925:
				world[(i,j)] = colors[pygame.K_s]
			elif i < 950:
				world[(i,j)] = colors[pygame.K_x]
			elif i < 975:
				world[(i,j)] = colors[pygame.K_e]
			else:
				world[(i,j)] = colors[pygame.K_d]
		elif j <= 75:
			if i % 25 == 0:
				world[(i,j)] = (200,200,200)
			elif i < 925:
				world[(i,j)] = colors[pygame.K_c]
			elif i < 950:
				world[(i,j)] = colors[pygame.K_r]
			elif i < 975:
				world[(i,j)] = colors[pygame.K_f]
			else:
				world[(i,j)] = colors[pygame.K_v]
		elif j <= 100:
			if i % 25 == 0:
				world[(i,j)] = (200,200,200)
			elif i < 925:
				world[(i,j)] = colors[pygame.K_t]
			elif i < 950:
				world[(i,j)] = colors[pygame.K_g]
			elif i < 975:
				world[(i,j)] = colors[pygame.K_b]
			else:
				world[(i,j)] = colors[pygame.K_y]
		elif j % 50 == 0 and j <= 400:
			world[(i,j)] = (200,200,200)
		elif j % 50 == 1 and j <= 401:
			world[(i,j)] = (150,150,150)
		elif j % 50 == 2 and j <= 402:
			world[(i,j)] = (100,100,100)
		else:
			world[(i,j)] = (170,170,170)
		if i == 900 or i == 1000:
			world[(i,j)] = (200,200,200)
		if i == 901 or i == 999:
			world[(i,j)] = (150,150,150)
		if i == 902 or i == 998:
			world[(i,j)] = (100,100,100)
#Line
ps = bresenham((925,140),(975,110))
for i in ps:
	world[i] = (0,0,0)
#Circle
ps = mid_point_circle((950,175),(950,190))
for i in ps:
	world[i] = (0,0,0)
#Polyline
ps  = bresenham((925,210),(950,240))
ps += bresenham((950,240),(975,230))
ps += bresenham((975,230),(975,220))
for i in ps:
	world[i] = (0,0,0)
#Curve
ps = bezier((925,260),(925,290),(975,260),(975,290))
for i in ps:
	world[i] = (0,0,0)
#Square
ps = rectangle((925,310),(975,340))
for i in ps:
	world[i] = (0,0,0)
#Fill
for i in range(925,976):
	for j in range(360,391):
		world[(i,j)] = (0,0,0)

#Init-------------------------------------------------------------------------------------------------
pygame.init()
screen = pygame.display.set_mode(size)
screen.fill(gray)
pygame.display.flip()

#Event handler----------------------------------------------------------------------------------------
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
				ms = pygame.mouse.get_pos()
				aux = handle_click(p1,ms,md,mc,pl,event.button)
#				print(aux)
				p1 = aux[0]
				md = aux[1]
				mc = aux[2]
				pl = aux[3]

	screen.fill(gray)

	for k in world.keys():
		screen.set_at(k,world[k])

	if p1 is not None:
		if   md == 1:
			ms = pygame.mouse.get_pos()
			ps = bresenham(p1,ms)
			for p in ps:
				screen.set_at(p,mc)
		elif md == 2:
			ms = pygame.mouse.get_pos()
			ps = mid_point_circle(p1,ms)
			for p in ps:
				screen.set_at(p,mc)
		elif md == 3:
			ms = pygame.mouse.get_pos()
			ps = bresenham(p1,ms)
			for p in ps:
				screen.set_at(p,mc)
		elif md == 4 and len(pl) == 3:
			ms = pygame.mouse.get_pos()
			ps = bezier(pl[0],pl[1],pl[2],ms)
			for p in ps:
				screen.set_at(p,mc)				
		elif md == 5:
			ms = pygame.mouse.get_pos()
			ps = rectangle(p1,ms)
			for p in ps:
				screen.set_at(p,mc)

	pygame.display.flip()

