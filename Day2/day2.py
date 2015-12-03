#Part1
sum = 0
file = open("day2.txt","r")
line = file.readline()
while(line != "\0"):
	line = line.rstrip("\n")
	if line == "":
		break
	line = line.split("x")
	sum1 = int(line[0])*int(line[1])
	sum2 = int(line[0])*int(line[2])
	sum3 = int(line[1])*int(line[2])
	sum += 2*sum1 + 2*sum2 + 2*sum3
	sum += min(sum1,sum2,sum3)
	line = file.readline()
print("Part1: "+str(sum))

#Part 2
sum = 0
file = open("day2.txt","r")
line = file.readline()
while(line != "\0"):
	line = line.rstrip("\n")
	if line =="":
		break
	line = line.split("x")
	sum += int(line[0])*int(line[1])*int(line[2]) #Bow
	min1 = min(int(line[0]),int(line[1]),int(line[2]))
	line.remove(str(min1))
	min2 = min(int(line[0]),int(line[1]))
	sum += 2*int(min1) + 2*int(min2)
	line = file.readline()
print("Part2: "+str(sum))

