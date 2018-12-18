with open("adjusts.txt", "r") as f:
	data = f.readlines()
	total = 0
	for line in data:
		op = line[0:1]
		if op == '+':
			total += int(line[1:])
		else:
			total -= int(line[1:])
	print(total)