#Part 1
floor = 0;
file = open("day1.txt","r")
code = file.readline()
for i in code:
	if i == '(':
		floor+=1
	else:
		floor-=1
print("Part1: "+str(floor))

#Part 2
floor = 0;
file = open("day1.txt","r")
code = file.readline()
for i in range(0,len(code)):
	if floor == -1:
		break
	if code[i] == '(':
		floor+=1
	else:
		floor-=1
print("Part2: "+str(i))