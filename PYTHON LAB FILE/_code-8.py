# Write text into a file using write() and writelines()
with open("output.txt", "w") as file:
    file.write("Python Programming\n")
    file.write("File Handling Example\n")
    lines = [
        "First line using writelines()\n",
        "Second line using writelines()\n",
        "Third line using writelines()\n"
    ]
    file.writelines(lines)
print("Data written successfully.")
# Read the file to verify its contents
with open("output.txt", "r") as file:
    print("\nFile Contents:")
    print(file.read())