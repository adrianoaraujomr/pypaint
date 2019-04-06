#!/usr/bin/python3

width,height = 990,540

def bresenham(p1,p2):
	pels = []
	inv = False
	neg = False

	print(p1)
	print(p2)

#Solve mirror problem x-axys --------------------------------------------------------------------------
	if p1[0] > p2[0]:
		aux = p1
		p1  = p2
		p2  = aux
#Solve mirror problem y-axys --------------------------------------------------------------------------
	if p1[1] > p2[1]:
		neg = True
		aux = (p2[0],height - p2[1])
		p2 = aux
#m == 0 -----------------------------------------------------------------------------------------------
	if p1[0] == p2[0]: #Check if p1 and p2 are in pels
			for i in range(p1[1],p2[1]):
				pels.append(p1[0],i)
				return pels
	elif p1[1] == p2[1]: #Check if p1 and p2 are in pels
			for i in range(p1[0],p2[0]):
				pels.append(i,p1[1])
				return pels
#------------------------------------------------------------------------------------------------------

	dx = p2[0] - p1[0]
	dy = p2[1] - p1[1]
	m  = dy/dx
	x = p1[0]
	y = p1[1]

	if m > 1: 
		inv = True
		dx = p2[1] - p1[1]
		dy = p2[0] - p1[0]
		x = p1[1]
		y = p1[0]

	print(p1)
	print(p2)
	print("m = " + str(dy/dx))

	dy2 = 2*dy
	pant = dy2 - dx
	dydx2 = dy2 - 2*dx
	
	pels.append(p1)

	for i in range(dx):
		if pant < 0:
			pels.append((x + 1,y))
			pant = pant + dy2
		else:
			pels.append((x + 1,y + 1))
			pant = pant + dydx2
			y += 1
		x += 1

	if inv:
		aux = []
		for i in pels:
			aux.append((i[1],i[0]))
		pels = aux
	if neg:
		aux = []
		for i in pels:
			aux.append((i[0],height - i[1]))
		pels = aux

	return pels
