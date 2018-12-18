with open("adjusts2.txt", "r") as f:
	data = f.readlines()
	f_i = 0
	f_s = ""
	for line1 in data:
		for line2 in data:
			diffs = 0
			diffindex = -1
			line1 = line1.strip()
			line2 = line2.strip()
			if line1 == line2:
				continue
			else:
				s = len(line1)
				for i in range(s):
					if line1[i] != line2[i]:
						diffs += 1
						diffindex = i
					if diffs > 1:
						break
				if diffs == 1:
					f_i = diffindex
					f_s = line1
	
	print(f_s[0:f_i] +  f_s[f_i+1:len(f_s)])