def read_text_file_into_lines(filename):
	return open(filename, "r", encoding="utf-8").read().splitlines()

from collections import defaultdict


final = read_text_file_into_lines("input.txt")
sample = read_text_file_into_lines("x.txt")
inputs = final

cc = 0
result = 0
x = 1
for inp in inputs:
	splits = inp.split(" ")
	if splits[0] == "noop":
		cc += 1
		if cc in [20, 60, 100, 140, 180, 220]:
			# print(cc, result, x)
			result += cc*x
	elif splits[0] == "addx":
		cc += 1
		if cc in [20, 60, 100, 140, 180, 220]:
			# print(cc, result, x)
			result += cc*x
		cc += 1
		if cc in [20, 60, 100, 140, 180, 220]:
			# print(cc, result, x)
			result += cc*x
		x += int(splits[1])


cc = -1
result = 0
x = 1
grid = [['.' for _ in range(40)] for _ in range(6)]

crow = 0
for i, inp in enumerate(inputs):
	splits = inp.split(" ")
	if splits[0] == "noop":
		cc += 1
		grid[cc//40][cc%40] = "#" if cc%40 in [x-1, x, x+1] else "."
	elif splits[0] == "addx":
		cc += 1
		grid[cc//40][cc%40] = "#" if cc%40 in [x-1, x, x+1] else "."
		cc += 1
		grid[cc//40][cc%40] = "#" if cc%40 in [x-1, x, x+1] else "."
		x += int(splits[1])



for i in range(6):
	print("".join(grid[i]))
	

