#!/usr/bin/python3

width,height = 990,540



#Pratically done, still need to confirm if p1 and p2 are on the line ##################################
def bresenham(p1,p2):
	pels = []
	inv = False
	neg = False

	print(p1)
	print(p2)
	print((p2[1] - p1[1])/(p2[0] - p1[0]))
	print("-----------------------------------------------------------")

#m == 0 -----------------------------------------------------------------------------------------------
	if p1[0] == p2[0]: #Check if p1 and p2 are in pels
			for i in range(p1[1],p2[1]):
				pels.append((p1[0],i))
				return pels
	elif p1[1] == p2[1]: #Check if p1 and p2 are in pels
			for i in range(p1[0],p2[0]):
				pels.append((i,p1[1]))
				return pels
#Solve mirror problem x-axys --------------------------------------------------------------------------
	if p1[0] > p2[0]:
		aux = p1
		p1  = p2
		p2  = aux
#Solve mirror problem y-axys --------------------------------------------------------------------------
	if p1[1] > p2[1]:
		print("Neg")
		neg = True
		base = p1
		p1 = (0,0)
		p2 = (p2[0] - base[0],(p2[1] - base[1])*(-1))
#------------------------------------------------------------------------------------------------------

	dx = p2[0] - p1[0]
	dy = p2[1] - p1[1]
	m  = dy/dx
	x = p1[0]
	y = p1[1]

	if m > 1: 
		print("Inv")
		inv = True
		dx = p2[1] - p1[1]
		dy = p2[0] - p1[0]
		x = p1[1]
		y = p1[0]

	dy2 = 2*dy
	pant = dy2 - dx
	dydx2 = dy2 - 2*dx
	
	pels.append((x,y))

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
			aux.append((i[0] + base[0],(i[1] * (-1)) + base[1]))
		pels = aux

	if p1 not in pels:
		print("No p1")
	if p2 not in pels:
		print("No p2")

	return pels
