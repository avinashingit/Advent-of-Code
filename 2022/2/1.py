def read_text_file_into_lines(filename):
	return open(filename, "r", encoding="utf-8").read().splitlines()



inputs = read_text_file_into_lines("input.txt")

d1 = {
	'X': 1, 
	"Y": 2,
	"Z": 3
}

d2 = {
	"win": 6,
	"draw": 3,
	"lose": 0
}
d3 = {
	"A": "X",
	"B": "Y",
	"C": "Z",
}

def find_result(x1, x2):
	if x2 == "X":
		if x1 == "B":
			return d2["lose"]
		return d2["win"]
	elif x2 == "Y":
		if x1 == "A":
			return d2["win"]
		return d2["lose"]
	else:
		if x1 == "B":
			return d2["win"]
		return d2["lose"]

score = 0
for inp in inputs:
	x1, x2 = inp.split(" ")
	score += d1[x2]
	print(inp, score)
	if d3[x1] == x2:
		score += d2["draw"]
		print("equa", score)
	else:
		score += find_result(x1, x2)
		print(score)
	print(score)

print(score)


score = 0
for inp in inputs:
	x1, x2 = inp.split(" ")
	if x2 == "X":
		score += d2["lose"]
		if x1 == "A":
			score += d1["Z"]
		elif x1 == "B":
			score += d1["X"]
		else:
			score += d1["Y"]
	elif x2 == "Y":
		score += d2["draw"]
		score += d1[d3[x1]]
	else:
		score += 6
		if x1 == "A":
			score += d1["Y"]
		elif x1 == "B":
			score += d1["Z"]
		else:
			score += d1["X"]

print(score) 