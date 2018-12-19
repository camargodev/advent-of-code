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

safe_area_size = 0
for i in range(maxy+2):
	for j in range(maxx+2):
		dist_counter = 0
		for point in points:
			dist_counter +=  manhattan_dist((j, i), point[1])
		if dist_counter < 10000:
			safe_area_size += 1
		M[j][i] = dist_counter

for i in range(maxy+2):
	line = ''
	for j in range(maxx+2):
		line += ' ' + str(M[j][i])
	print(line)

print(safe_area_size)
				