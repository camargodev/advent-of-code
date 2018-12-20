import sys

numbers = []

with open("input", "r") as f:
	data = f.readlines()
	numbers = [int(x) for x in data[0].split()]

def get_total(numbers):
	num_children = numbers[0] 
	num_data = numbers[1] 
	remaining = numbers[2:]
	children = []

	for i in range(num_children):
		total_child, remaining = get_total(remaining)
		children.append(total_child) 

	if num_children == 0:
		return sum(remaining[:num_data]), remaining[num_data:]
	else:
		total = 0
		for child in remaining[:num_data]:
			i = child-1
			if i >= 0 and i < len(children):
				total += children[i]
		return total, remaining[num_data:]		

total, _ = get_total(numbers)
print(total)
