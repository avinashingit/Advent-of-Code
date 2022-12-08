def read_text_file_into_lines(filename):
	return open(filename, "r", encoding="utf-8").read().splitlines()


final = read_text_file_into_lines("input.txt")
sample = read_text_file_into_lines("x.txt")
inputs = final

inp_len = len(inputs[0])
grid = []
for row in inputs:
	grid.append(list(row))

count = 0
count += len(grid[0])
count += len(grid[-1])
count += (len(grid)-2)*2

for i in range(1, len(grid)-1):
	# print(i)
	for j in range(1, len(grid[0])-1):
		height = int(grid[i][j])

		r, column = grid[i], []
		for row in grid:
			column.append(row[j])
		if height > int(max(r[:j])):
			count += 1
		elif height > int(max(r[j+1:])):
			count += 1
		elif height > int(max(column[i+1:])):
			count += 1
		elif height > int(max(column[:i])):
			count += 1

print(count)


cscore = 1
mscore = cscore
for i in range(0, len(grid)):
	for j in range(0, len(grid[0])):
		height = grid[i][j]
		row, column = grid[i], []
		for x in grid:
			column.append(x[j])
		left, right, top, bottom = 0, 0, 0, 0
		if i == 0 or j == 0:
			cscore = 0
			continue
		for l in range(j-1, -1, -1):
			if row[l] < height:
				left += 1
			else:
				left += 1
				break
		for r in range(j+1, len(row)):
			if row[r] < height:
				right += 1
			else:
				right += 1
				break

		for t in range(i-1, -1, -1):
			if column[t] < height:
				top += 1
			else:
				top += 1
				break

		for b in range(i+1, len(column)):
			if column[b] < height:
				bottom += 1
			else:
				bottom += 1
				break
		cscore = left*right*top*bottom
		mscore = max(mscore, cscore)

print(mscore)

