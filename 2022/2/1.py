def read_text_file_into_lines(filename):
	return open(filename, "r", encoding="utf-8").read().splitlines()



inputs = read_text_file_into_lines("input.txt")

p1 = {
	"A": 0,
	"B": 1,
	"C": 2
}

p2 = {
	"X": 0,
	"Y": 1, 
	"Z": 2,
}


d2 = {
	"win": 6,
	"draw": 3,
	"lose": 0
}

def find_result(x1, x2):
	i1 = p1[x1]
	i2 = p2[x2]
	if (i1 + 1)%3 == i2:
		return d2["win"]
	return d2["lose"]

score = 0
for inp in inputs:
	x1, x2 = inp.split(" ")
	score += p2[x2] + 1
	if p1[x1] == p2[x2]:
		score += d2["draw"]
	else:
		score += find_result(x1, x2)

print(score)


score = 0
for inp in inputs:
	x1, x2 = inp.split(" ")
	if x2 == "X":
		score += d2["lose"]
		score += (p1[x1]+2)%3+1
	elif x2 == "Y":
		score += d2["draw"]
		score += p1[x1]+1
	else:
		score += 6
		score += (p1[x1]+1)%3+1

print(score) 