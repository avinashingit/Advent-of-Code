def read_text_file_into_lines(filename):
	return open(filename, "r", encoding="utf-8").read().splitlines()


inputs = read_text_file_into_lines("input.txt")
score = 0
for inp in inputs:
	l = len(inp)
	x1, x2 = inp[:l//2], inp[l//2:]
	x1 = set(x1)
	x2 = set(x2)
	common = []
	for x in x1:
		if x in x2:
			common.append(x)
	for x in common:
		if x.islower():
			score += ord(x)-97+1
		else:
			score += ord(x)-65+27

print(score)

score = 0

def find_common(a, b, c):
	return set(set(a).intersection(set(b))).intersection(set(c))

l = len(inputs)
for i in range(0, l, 3):
	x = find_common(inputs[i], inputs[i+1], inputs[i+2])
	x = list(x)[0]
	if x.islower():
		score += ord(x)-97+1
	else:
		score += ord(x)-65+27

print(score)