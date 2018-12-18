code = ''

with open("input", "r") as f:
	data = f.readlines()
	for line in data:
		code += line

code = code.strip()
has_changes = True

while has_changes:
	for i in range(len(code)-1):
		if code[i] != code[i+1]:
			if code[i].lower() == code[i+1].lower():
				code = code[:i] + code[i+2:]
				break
		if i == len(code)-2:
			has_changes = False

print(len(code))


				