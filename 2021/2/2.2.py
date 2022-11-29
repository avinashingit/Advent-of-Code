with open("input.txt", "r") as f:
	inputs = f.readlines()

inputs = [inp.strip().split(" ") for inp in inputs]
aim, distance, depth = 0, 0, 0

for inp in inputs:
	if inp[0] == "forward":
		distance += int(inp[1])
		depth += aim*int(inp[1])
	elif inp[0] == "up":
		aim -= int(inp[1])
	else:
		aim += int(inp[1])

print(distance, depth, distance*depth)