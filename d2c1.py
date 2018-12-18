with open("adjusts2.txt", "r") as f:
	data = f.readlines()
	count2 = 0
	count3 = 0
	for line in data:
		added2 = False
		added3 = False
		for c in line:
			if line.count(c) == 2:
				added2 = True
			if line.count(c) == 3:
				added3 = True
		if added2:
			count2 += 1
		if added3:
			count3 += 1
	print(count2 * count3)