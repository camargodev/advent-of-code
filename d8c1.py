import sys

numbers = []

with open("input", "r") as f:
	data = f.readlines()
	numbers = [int(x) for x in data[0].split()]

def get_total(numbers):
	num_children = numbers[0] 
	num_data = numbers[1] 
	remaining = numbers[2:]
	total = 0

	for i in range(num_children):
		t, remaining = get_total(remaining)
		total += t

	total += sum(remaining[:num_data])

	return total, remaining[num_data:]

total, _ = get_total(numbers)
print(total)
