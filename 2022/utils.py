def read_text_file_into_lines(filename):
	return open(filename, "r", encoding="utf-8").read().splitlines()