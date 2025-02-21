from getpass import getpass

# Prompt for username
username = input("Enter Username: ")

# Prompt for password securely
password = getpass("Enter password: ")

# Simple validation
if len(username) == 0:
    print("Username cannot be empty!")
elif len(password) < 6:
    print("Password must be at least 6 characters long!")
else:
    print("Username and password are valid.")