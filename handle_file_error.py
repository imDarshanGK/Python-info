from contextlib import suppress

file_name = "missing_file.txt" 
with suppress(FileNotFoundError):
    open(file_name)

print("After with block")
