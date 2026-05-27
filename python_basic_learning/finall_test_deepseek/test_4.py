# Write a program that takes a file name as input from the user, 
# reads the file, and outputs the number of lines in the file.
from pathlib import Path

file_name = input("Input name of file: ")
print(file_name)
path = Path(file_name)

try:
    contents = path.read_text()
    lines = contents.splitlines()
    count_lines = len(lines)
    print(f"Count of lines in file: {count_lines}")
except FileNotFoundError:
    print(f"Not found file: {file_name}")