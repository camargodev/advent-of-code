def parse_line(line):
	id, data = line.split('@')
	pos, size = data.strip().split(':')
	x, y = pos.strip().split(',')
	w, h = size.strip().split('x')
	return str(id.strip()), int(x), int(y), int(w), int(h)
	
ids = []
xs = []
ys = []
ws = []
hs = []
total_w = 0
total_h = 0

with open("adjusts2.txt", "r") as f:
	data = f.readlines()
	for line in data:
		id, x, y, w, h = parse_line(line)
		ids.append(id)
		xs.append(x)
		ys.append(y)
		ws.append(w)
		hs.append(h)
		if x+w > total_w:
			total_w = x+w
		if y+h > total_h:
			total_h = y+h
			
total_w += 2
total_h += 2

M = [[0 for x in range(total_w)] for y in range(total_h)]
for i in range(len(xs)):
	x, y, w, h = xs[i], ys[i], ws[i], hs[i]
	for wi in range(w):
		for hi in range(h):
			M[x+wi][y+hi] += 1
		
valid_ids = []		
for i in range(len(xs)):
	x, y, w, h = xs[i], ys[i], ws[i], hs[i]
	valid = True
	for wi in range(w):
		for hi in range(h):
			if M[x+wi][y+hi] > 1:
				valid = False
	if valid:
		valid_ids.append(ids[i])
		
print(valid_ids)


				