with open("input.txt", "r") as f:
	inputs = f.readlines()

inputs = [int(inp.strip()) for inp in inputs]

csum = 0
csum += inputs[0]
csum += inputs[1]
csum += inputs[2]

x = 0
count = 0
for i in range(3, len(inputs)):
	if csum - inputs[x] + inputs[i] > csum:
		count += 1
	csum += inputs[i] - inputs[x]
	x += 1
print(count)1.2.py