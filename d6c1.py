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
	mayy = max(y, mayy)

M = [[0 for x in range(maxx+1)] for y in range(maxy+1)]

for i in range(maxx+1):
	for j in range(maxy+1):
		closest = None
		for point in points:


				