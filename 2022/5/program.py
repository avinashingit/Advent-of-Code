def read_text_file_into_lines(filename):
	return open(filename, "r", encoding="utf-8").read().splitlines()


inputs = read_text_file_into_lines("input.txt")

from collections import defaultdict
d = defaultdict(list)

d = {
	1: ['R', 'N', 'F', 'V', 'L', 'J', 'S', 'M'],
	2: ['P', 'N', 'D', 'Z', 'F', 'J', 'W', 'H'],
	3: ['W', 'R', 'C', 'D', 'G'],
	4: ['N', 'B', 'S'],
	5: ['M', 'Z', 'W', 'P', 'C', 'B', 'F', 'N'],
	6: ['P', 'R', 'M', 'W'],
	7: ['R', 'T', 'N', 'G', 'L', 'S', 'W'],
	8: ['Q', 'T', 'H', 'F', 'N', 'B', 'V'],
	9: ['L', 'M', 'H', 'Z', 'N', 'F']
}

# racks = inputs['8'].split("   ")
# for inp in inputs[':8']:
# 	splits = inp.split(" ")
# 	print(splits)
# 	for i', 'split in enumerate(splits):
# 		if split != "":
# 			d['i+1'].append(split)

# for k', 'v in d.items():
# 	d['k'] = v['::-1']
# 	print(k', 'len(v))


for inp in inputs[10:]:
	splits = inp.split(' ')
	print(splits)
	count = int(splits[1])
	sr = int(splits[3])
	dr = int(splits[5])
	X = []
	for i in range(count):
		x = d[sr].pop()
		X.append(x)
	d[dr].extend(X[::-1])

s = []
for k, v in d.items():
	print(v[-1])
	s.append(v[-1])
print("".join(s))