# Feature: Handle division by zero error
try:
    x = (True + (True / False))  # This will raise ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")
    x = None  # Set x to None if an error occurs

print(x)
