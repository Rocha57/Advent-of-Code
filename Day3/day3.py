#Soluçoes mesmo à porco
#Part 1
file = open("day3.txt","r")
line = file.readline()
casasPercorridas = [[0,0]]
posicaoAnterior = [0,0]
posicaoActualx = 0
posicaoActualy = 0
for car in line:
	if car == "^":
		posicaoActualy = posicaoAnterior[1]+1
	elif car == "<":
		posicaoActualx = posicaoAnterior[0]-1
	elif car == "v":
		posicaoActualy = posicaoAnterior[1]-1
	else:
		posicaoActualx = posicaoAnterior[0]+1
	tuplo = (posicaoActualx, posicaoActualy)
	if casasPercorridas.count(tuplo) == 0:
		casasPercorridas.append(tuplo)
	posicaoAnterior[0] = posicaoActualx
	posicaoAnterior[1] = posicaoActualy

print("Part1: "+ str(len(casasPercorridas)-1))

#Part 2
file = open("day3.txt","r")
line = file.readline()
casasPercorridas = [[0,0]]
posicaoAnteriorSanta = [0,0]
posicaoAnteriorRobot = [0,0]
posicaoActualSantax = 0
posicaoActualSantay = 0
posicaoActualRobotx = 0
posicaoActualRoboty = 0
i = 0
for car in line:
	if i%2 == 0:
		print(car)
		if car == "^":
			posicaoActualSantay = posicaoAnteriorSanta[1]+1
		elif car == "<":
			posicaoActualSantax = posicaoAnteriorSanta[0]-1
		elif car == "v":
			posicaoActualSantay = posicaoAnteriorSanta[1]-1
		elif car == ">":
			posicaoActualSantax = posicaoAnteriorSanta[0]+1
		tuplo = (posicaoActualSantax, posicaoActualSantay)
		if casasPercorridas.count(tuplo) == 0:
			casasPercorridas.append(tuplo)
		posicaoAnteriorSanta[0] = posicaoActualSantax
		posicaoAnteriorSanta[1] = posicaoActualSantay
		print("Santa: " + str(posicaoAnteriorSanta))
		i+=1
	elif i%2 == 1:
		if car == "^":
			posicaoActualRoboty = posicaoAnteriorRobot[1]+1
		elif car == "<":
			posicaoActualRobotx = posicaoAnteriorRobot[0]-1
		elif car == "v":
			posicaoActualRoboty = posicaoAnteriorRobot[1]-1
		elif car == ">":
			posicaoActualRobotx = posicaoAnteriorRobot[0]+1
		tuplo = (posicaoActualRobotx, posicaoActualRoboty)
		if casasPercorridas.count(tuplo) == 0:
			casasPercorridas.append(tuplo)
		posicaoAnteriorRobot[0] = posicaoActualRobotx
		posicaoAnteriorRobot[1] = posicaoActualRoboty
		i+=1
print(len(casasPercorridas)-1)