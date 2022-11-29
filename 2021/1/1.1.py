with open("input.txt", "r") as f:
	inputs = f.readlines()
print(inputs)

inputs = [int(inp.strip()) for inp in inputs]
count = 0
for i in range(1, len(inputs)):
	if inputs[i] > inputs[i-1]:
		count += 1
print(count)