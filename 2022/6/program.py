def read_text_file_into_lines(filename):
	return open(filename, "r", encoding="utf-8").read().splitlines()


inputs = read_text_file_into_lines("input.txt")[0]
for i in range(0, len(inputs)-4):
	if len(set(inputs[i:i+4])) == 4:
		print(i+4)
		break

for i in range(0, len(inputs)-14):
	if len(set(inputs[i:i+14])) == 14:
		print(i+14)
		break