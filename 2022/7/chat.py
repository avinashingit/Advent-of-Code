# Create a class to represent a file or directory in the filesystem.
class FileSystemObject:
  def __init__(self, name, size=0, children=None):
    self.name = name
    self.size = size
    self.children = [] if children is None else children

  def __str__(self):
    return f"{self.name} ({self.size})"

# Parse the given terminal output and return a tree representing the filesystem.
def parse_output(output):
  # Split the output into lines.
  lines = output.strip().split("\n")

  # Create a stack to keep track of the current directory and its parent directories.
  # We will use this stack to build the tree representation of the filesystem.
  stack = [FileSystemObject("/")]

  # Iterate over the lines of output.
  for line in lines:
    # If the line starts with "$ cd", it is a change directory command.
    if line.startswith("$ cd"):
      # Split the line on whitespace to get the command and its argument.
      _, command, argument = line.split()

      # If the argument is "..", move up one level in the directory tree.
      # Otherwise, move down one level and add a new child to the current directory.
      if argument == "..":
        stack.pop()
      else:
        new_dir = FileSystemObject(argument)
        stack[-1].children.append(new_dir)
        stack.append(new_dir)

    # If the line starts with "$ ls", it is a list command.
    elif line.startswith("$ ls"):
      # Split the line on whitespace to get the command and its argument.
      _, command, argument = line.split()

      # The argument will be a list of files and directories in the current directory.
      # Split the argument on whitespace to get the names of the files and directories.
      names = argument.split()

      # Iterate over the names and create FileSystemObject instances for each one.
      # Add these objects as children of the current directory.
      for name in names:
        # If the name ends with ".txt", ".dat", ".log", or ".ext", it is a file.
        # Otherwise, it is a directory.
        if name.endswith((".txt", ".dat", ".log", ".ext")):
          file_size = int(name.split(".")[0])
          new_file = FileSystemObject(name, file_size)
          stack[-1].children.append(new_file)
        else:
          new_dir = FileSystemObject(name)
          stack[-1].children.append(new_dir)

  # After processing all lines of output, the root of the tree will be the top item
  # on the stack. Return it as the result of the function.
  return stack[0]

# Calculate the total size of a directory by summing the sizes of all files it
# contains, directly or indirectly.
def total_size(directory):
  # Start the total size at 0.
  total = 0

  # Recursively calculate the total sizes of all child directories.
  for child in directory.