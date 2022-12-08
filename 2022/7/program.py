def read_text_file_into_lines(filename):
	return open(filename, "r", encoding="utf-8").read().splitlines()


inputs = read_text_file_into_lines("x.txtr")

class Directory:
	def __init__(self, directory_name):
		self.contents = {
			directory_name: {}
		}

directory_objects = []
for inp in inputs[1:]:
	if inp[0] == '$':
		if inp[2:4] == "cd":
			directory_name = inp[5:]
			if directory_name == "/":
				directory_objects.append(Directory("/"))
			elif directory_name == "..":
				directory_objects.pop()
			else:
				directory_objects.append(Directory(directory_name))
	else:
		if inp[:3] == "dir":
			directory_objects[-1].directories.append(Directory(inp[4:]))
		else:
			command_split = inp.split(" ")
			directory_objects[-1].files.append(command_split[0])

print(current_directory)

