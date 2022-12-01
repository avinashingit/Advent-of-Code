inputs = open("input.txt", "r").read().splitlines()

totals = []
csum = 0
for inp in inputs:
	if inp == "":
		totals.append(csum)
		csum = 0
	else:
		csum += int(inp)

print(max(totals))
totals.sort()
print(sum(totals[-3:]))