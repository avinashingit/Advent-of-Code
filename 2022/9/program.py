def read_text_file_into_lines(filename):
	return open(filename, "r", encoding="utf-8").read().splitlines()

from collections import defaultdict


final = read_text_file_into_lines("input.txt")
sample = read_text_file_into_lines("x.txt")
inputs = final

grid_size = 0
for row in inputs:
	x, y = row.split(" ")
	grid_size = max(grid_size, int(y))

row = {
	"L": 0, 
	"R": 0,
	"U": -1,
	"D": 1
}

column = {
	"L": -1,
	"R": 1,
	"U": 0,
	"D": 0,
}

def find_tail(h, t):
	if abs(h[0]-t[0]) <= 1 and abs(h[1]-t[1]) <= 1:
		return t
	elif abs(h[0]-t[0]) >= 2 and abs(h[1]-t[1]) >= 2:
		return (h[0]-1 if h[0] > t[0] else h[0] + 1, h[1] - 1 if h[1] > t[1] else h[1] + 1)
	elif abs(h[0]-t[0]) >= 2:
		return (h[0]-1 if h[0] > t[0] else h[0] + 1, h[1])
	elif abs(h[1] - t[1]) >= 2:
		return (h[0], h[1] - 1 if h[1] > t[1] else h[1] + 1)

hpos = (0, 0)
tpos = (0, 0)
positions = defaultdict(int)
for inp in inputs:
	x, y = inp.split(" ")
	y = int(y)
	for _ in range(y):
		hpos = (hpos[0] + row[x], hpos[1] + column[x])
		tpos = find_tail(hpos, tpos)
		positions[tpos] += 1

print(len(positions.keys()))


hpos = (0, 0)
tpos = [(0, 0) for i in range(9)]
positions = defaultdict(int)
for inp in inputs:
	x, y = inp.split(" ")
	y = int(y)
	for _ in range(y):
		hpos = (hpos[0] + row[x], hpos[1] + column[x])
		tpos[0] = find_tail(hpos, tpos[0])
		for i in range(1, 9):
			tpos[i] = find_tail(tpos[i-1], tpos[1])
		positions[tpos[8]] += 1

print(len(positions.keys()))



