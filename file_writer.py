with open("test.txt", "w") as file:
    file.write("Hello!")

# Check if the file is closed after the 'with' block automatically closes it
print(file.closed)
