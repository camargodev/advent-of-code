with open("adjusts.txt", "r") as f:
	data = f.readlines()
	total = 0
	found = False
	already_seens = []
	already_seens.append(total)
	while not found:
		for line in data:
			op = line[0:1]
			if op == '+':
				total += int(line[1:])
			else:
				total -= int(line[1:])
			if total in already_seens:
				print(total)
				found = True
				break
			else:
				already_seens.append(total)
			