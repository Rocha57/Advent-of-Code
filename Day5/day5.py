#PART1

file = open('day5.txt','r')
lines = file.readlines()
nice_counter = 0

for line in lines:
	i = 0
	if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
		continue
	vogals = line.count('a') + line.count('e') + line.count('i') + line.count('o') + line.count('u')
	if vogals < 3:
		continue
	for i in range(len(line)-1):
		if (line[i] == line[i+1]):
			nice_counter+=1
			break

print(nice_counter)

#PART2

file = open('day5.txt','r')
lines = file.readlines()
nice_counter = 0
candidates  = []

for line in lines:
	for i in range(len(line)-1):
		if (line.count(line[i]+line[i+1]) > 1):
			candidates.append(line)
			break
			
for x in candidates:
	for i in range(len(x)-2):
		if (x[i] == x[i+2]):
			nice_counter+=1
			break

print(nice_counter)