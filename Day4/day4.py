#PART 1

from hashlib import md5

key = 'iwrupvqb'
i = 1;
while i > 0:
	hashcode = md5((key + str(i)).encode()).hexdigest()
	if hashcode[:5] == '00000':
		print(i)
		break
	i+=1

#PART2

from hashlib import md5

key = 'iwrupvqb'
i = 1;
while i > 0:
	hashcode = md5((key + str(i)).encode()).hexdigest()
	if hashcode[:6] == '000000':
		print(i)
		break
	i+=1