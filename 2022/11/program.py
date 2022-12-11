def read_text_file_into_lines(filename):
	return open(filename, "r", encoding="utf-8").read().splitlines()

from collections import defaultdict
import math


final = read_text_file_into_lines("input.txt")
sample = read_text_file_into_lines("x.txt")
inputs = final

monkey_items = {
	0: [85, 77, 77],
	1: [80, 99],
	2: [74, 60, 74, 63, 86, 92, 80],
	3: [71, 58, 93, 65, 80, 68, 54, 71],
	4: [97, 56, 79, 65, 58],
	5: [77],
	6: [99, 90, 84, 50],
	7: [50, 66, 61, 92, 64, 78]
}
operations = {
	0: ["*", 7],
	1: ["*", 11],
	2: ["+", 8],
	3: ["+", 7],
	4: ["+", 5],
	5: ["+", 4],
	6: ["**", 2],
	7: ["+", 3]
}

divisibility = {
	0: 19,
	1: 3,
	2: 13,
	3: 7,
	4: 5,
	5: 11,
	6: 17, 
	7: 2,
}
action = {
	0: [6, 7],
	1: [3, 5],
	2: [0, 6],
	3: [2, 4],
	4: [2, 0],
	5: [4, 3],
	6: [7, 1],
	7: [5, 1]
}


def get_new_level(value, operation):
	if operation[0] == "*":
		return value * operation[1]
	elif operation[0] == "+":
		return value + operation[1]
	elif operation[0] == "**":
		return value ** 2

counts = defaultdict(int)

rounds = 20
for r in range(rounds):
	for mnum, items in monkey_items.items():
		while items[::-1]:
			item = items.pop()
			new_value = get_new_level(item, operations[mnum])
			new_value //= 3
			if new_value%divisibility[mnum] == 0:
				monkey_items[action[mnum][0]].append(new_value)
			else:
				monkey_items[action[mnum][1]].append(new_value)
			counts[mnum] += 1

print(counts)


counts = defaultdict(int)

monkey_items = {
	0: [85, 77, 77],
	1: [80, 99],
	2: [74, 60, 74, 63, 86, 92, 80],
	3: [71, 58, 93, 65, 80, 68, 54, 71],
	4: [97, 56, 79, 65, 58],
	5: [77],
	6: [99, 90, 84, 50],
	7: [50, 66, 61, 92, 64, 78]
}
rounds = 10000
for r in range(rounds):
	for mnum, items in monkey_items.items():
		while items[::-1]:
			item = items.pop()
			new_value = get_new_level(item, operations[mnum])
			new_value %= (2*3*5*7*11*13*17*19)
			if new_value%divisibility[mnum] == 0:
				monkey_items[action[mnum][0]].append(new_value)
			else:
				monkey_items[action[mnum][1]].append(new_value)
			counts[mnum] += 1

print(counts)

