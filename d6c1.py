def manhattan_dist(p, q):
	distx = abs(p[0] - q[0])
	disty = abs(p[1] - q[1])
	return distx + disty

points = []
maxx = 0
maxy = 0

with open("input", "r") as f:
	data = f.readlines()
	counter = 0
	for line in data:
		x, y = line.split(',')
		x, y = int(x), int(y)
		points.append((counter, (x, y)))
		counter += 1

for point in points:
	x, y = point[1]
	maxx = max(x, maxx)
	maxy = max(y, maxy)

M = [[None for x in range(maxy+2)] for y in range(maxx+2)]

for point in points:
	x, y = point[1]
	M[y][x] = point[0]

for i in range(maxy+1):
	for j in range(maxx+1):
		closest = None
		closest_dist = 0
		counter = 0
		for point in points:
			dist = manhattan_dist((j, i), point[1])
			#print(i, j, dist)
			if closest == None:
				closest = point[0]
				closest_dist = dist
			elif closest_dist > dist:
				closest = point[0]
				closest_dist = dist
		for point in points:
			dist = manhattan_dist((j, i), point[1])
			if dist == closest_dist:
				counter += 1
		if counter > 1:
			closest = None
		M[i][j] = closest

for i in range(maxy+1):
	line = ''
	for j in range(maxx+1):
		line += ' '
		line += '.' if M[i][j] == None else str(M[i][j])
	print(line)


				