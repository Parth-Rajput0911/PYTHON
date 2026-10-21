# Create a sample text file
with open("sample.txt", "w") as file:
    file.write("Welcome to Python Programming.\n")
    file.write("Python is easy to learn.\n")
    file.write("File handling is useful.\n")
# Read the complete file
with open("sample.txt", "r") as file:
    print("Using read():")
    print(file.read())
# Read one line
with open("sample.txt", "r") as file:
    print("Using readline():")
    print(file.readline(), end="")
# Read all lines into a list
with open("sample.txt", "r") as file:
    print("\nUsing readlines():")
    lines = file.readlines()
    print(lines)