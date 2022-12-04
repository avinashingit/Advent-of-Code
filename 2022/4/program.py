def read_text_file_into_lines(filename):
	return open(filename, "r", encoding="utf-8").read().splitlines()


inputs = read_text_file_into_lines("input.txt")


def check(s1, e1, s2, e2):
	if s1 <= s2 and e2<=e1:
		return 1
	if s2 <= s1 and e2 >= e1:
		return 1
	return 0


def check_overlap(s1, e1, s2, e2):
	if s1 in range(s2, e2+1) or e1 in range(s2, e2+1) or s2 in range(s1, e1+1) or e2 in range(s1, e1+1):
		return 1
	return 0

s = 0
for inp in inputs:
	r1, r2 = inp.split(",")
	r1s, r1e = r1.split("-")
	r2s, r2e = r2.split("-")
	s += check(int(r1s), int(r1e), int(r2s), int(r2e))

print(s)

s = 0
for inp in inputs:
	r1, r2 = inp.split(",")
	r1s, r1e = r1.split("-")
	r2s, r2e = r2.split("-")
	s += check_overlap(int(r1s), int(r1e), int(r2s), int(r2e))

print(s)
