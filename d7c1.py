import copy

pre_reqs = dict()
next_steps = dict()
steps = []

def parse(line):
	line = line.replace("Step ", "")
	line = line.replace("must be finished before step ", "")
	line = line.replace(" can begin.", "")
	req, step = line.split(' ')
	step = step.strip()
	return req, step

def get_steps_available():
	available = []
	for step in steps:
		if step not in pre_reqs:
			available.append(step)
	return available

def reduction():
	for step1 in steps:
		for step2 in steps:
			if step1 == step2:
				continue


with open("input", "r") as f:
	data = f.readlines()
	for line in data:
		req, step = parse(line)
		if req not in steps:
			steps.append(req)
		if step not in steps:
			steps.append(step)
		if step not in pre_reqs.keys():
			pre_reqs[step] = []
		if req not in next_steps.keys():
			next_steps[req] = []
		pre_reqs[step].append(req)
		next_steps[req].append(step)

path = []

#for s in next_steps.keys():
#	print("Next steps for " + s +" are = " + str(next_steps[s]))
while steps:
	available = get_steps_available()
	available.sort()
	for step in steps:
		if step in pre_reqs:
			print("Pre reqs for " + step + " are = " + str(pre_reqs[step]))
		else:
			print("Pre reqs for " + step + " are = []")
	print("Available are " + str(available))
	step = None
	if not available:
		steps.sort()
		for s in steps:
			for req in pre_reqs[s]:
				if req not in path:
					break
			step = steps[0]
	else:	
		step = available[0]
	if step is None:
		break
	path.append(step) 
	del steps[steps.index(step)]
	print("Selected = " + step)
	#print("Steps is now = " + str(steps))
	tmp_reqs = dict()
	for req in pre_reqs:
		if step in pre_reqs[req]:
			del pre_reqs[req][pre_reqs[req].index(step)]
	for req in pre_reqs:
		if pre_reqs[req]:
			tmp_reqs[req] = pre_reqs[req]
	pre_reqs = copy.deepcopy(tmp_reqs)
	print(path)
	#print("Pre reqs are now = " + str(pre_reqs))

#print(path)
final = ''
for p in path:
	final += str(p)
print(final)