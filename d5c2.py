code = ''
alphabet = []

with open("input", "r") as f:
	data = f.readlines()
	for line in data:
		code += line

code = code.strip()

for gene in code:
	if gene.lower() not in alphabet:
		alphabet.append(gene.lower())

min_size = None

for gene in alphabet:
	new_code = code
	new_code = new_code.replace(gene, "")
	new_code = new_code.replace(gene.upper(), "")
	has_changes = True
	while has_changes:
		for i in range(len(new_code)-1):
			if new_code[i] != new_code[i+1]:
				if new_code[i].lower() == new_code[i+1].lower():
					new_code = new_code[:i] + new_code[i+2:]
					break
			if i == len(new_code)-2:
				has_changes = False
	if min_size == None:
		min_size = len(new_code)
	else:
		min_size = min(min_size, len(new_code))

print(min_size)


				