import copy

NUM_WORKERS = 5

pre_reqs = dict()
steps = []
alphabet = 'abcdefghijklmnopqrstuvwxyz'
total_time = -1
workers = [None for i in range(NUM_WORKERS)]
rem_time = [-1 for i in range(NUM_WORKERS)]

def parse(line):
	line = line.replace("Step ", "")
	line = line.replace("must be finished before step ", "")
	line = line.replace(" can begin.", "")
	req, step = line.split(' ')
	step = step.strip()
	return req, step

def get_steps_available(steps, reqs):
	available = []
	for step in steps:
		if step not in reqs:
			available.append(step)
	return available

def get_duration(letter):
	low = letter.lower().strip()
	basis = 60
	letter_duration = alphabet.index(low) + 1
	return basis + letter_duration

def get_first_free_worker(pworkers):
	size = len(pworkers)
	for i in range(size):
		if pworkers[i] == None:
			return i
	return None

def print_moment():
	msg = 'At ' + str(total_time) + ':'
	for i in range(NUM_WORKERS):
		msg += '\n  W' + str(i)
		msg += ' in ' + str(workers[i]) 
		msg += '. Rem: ' + (str(rem_time[i]) + 's' if rem_time[i] != -1 else '-')
	print(msg)

def delete_step(reqs, steps, step):
	if steps and step is not None:
		del steps[steps.index(step)]
	tmp_reqs = dict()
	for req in reqs:
		if step in reqs[req]:
			del reqs[req][reqs[req].index(step)]
	for req in reqs:
		if reqs[req]:
			tmp_reqs[req] = reqs[req]
	return copy.deepcopy(tmp_reqs), copy.deepcopy(steps)

def compute_tasks(time, reqs, steps):
	for w in range(NUM_WORKERS):
		if rem_time[w] != -1:
			if rem_time[w] > 0:
				rem_time[w] -= 1
			if rem_time[w] == 0:
				reqs, steps = delete_step(reqs, steps, workers[w])
				workers[w] = None
	return time + 1, reqs, steps

def check_max_rem_time(rem_time):
	tmp_rem_time = []
	for t in rem_time:
		if t != -1:
			tmp_rem_time.append(t)
	if not tmp_rem_time:
		return True
	else:
		return max(tmp_rem_time) > 0

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
		pre_reqs[step].append(req)

started = []

while steps or check_max_rem_time(rem_time):
	total_time, pre_reqs, steps = compute_tasks(total_time, pre_reqs, steps)
	free_worker = get_first_free_worker(workers)
	if free_worker is not None:
		available = get_steps_available(steps, pre_reqs)
		available.sort()
		print(available)
		for step in available:
			if free_worker is None:
				break
			if step in started:
				continue
			duration = get_duration(step)
			workers[free_worker] = step
			rem_time[free_worker] = duration
			started.append(step)
			free_worker = get_first_free_worker(workers) 
	print_moment()

print(total_time)