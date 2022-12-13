def read_text_file_into_lines(filename):
	return open(filename, "r", encoding="utf-8").read().splitlines()

from collections import defaultdict
import math


final = read_text_file_into_lines("input.txt")
sample = read_text_file_into_lines("x.txt")
inputs = final


grid = []
temp = []
sr, sc = None, None
for i, inp in enumerate(inputs):
	for j, split in enumerate(list(inp)):
		if split == "S":
			temp.append("a")
			sr, sc = i, j
		else:
			temp.append(split)
	grid.append(temp)
	temp = []


S= set()
def dfs(r, c, x, y, prev, length, grid):
	if (r, c) in S:
		return
	print(r, c, x, y)
	if r >= x or c >= y:
		return
	if ord(grid[r][c]) - ord(prev) > 1:
		return
	if ord(grid[r][c]) == "E":
		return length

	left = dfs(r, c-1, x, y, grid[r][c], length+1, grid)
	right = dfs(r, c+1, x, y, grid[r][c], length+1, grid)
	top = dfs(r-1, c, x, y, grid[r][c], length+1, grid)
	bottom = dfs(r+1, c, x, y, grid[r][c], length+1, grid)

	S.add((r, c))

	return min(
		dfs(r-1, c, x, y, grid),
		dfs(r+1, c, x, y, grid),
		dfs(r, c+1, x, y, grid),
		dfs(r, c-1, x, y, grid)
	)

print(dfs(sr, sc, len(grid), len(grid[0]), "a", 0, grid))