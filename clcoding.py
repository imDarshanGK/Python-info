# Example 1: Direct floating-point comparison
a = 0.2 + 0.4
b = 0.6
print(a == b)  # This will output False due to floating-point precision issues

# Example 2: A similar issue with other numbers
x = 0.1 + 0.3
y = 0.4
print(x == y)  # This will also output False for the same reason

# Correct way to compare floating-point numbers
epsilon = 1e-9  # Define a small tolerance value

# Use the tolerance to compare
print(abs(a - b) < epsilon)  # This should print True, as the difference is within the tolerance
print(abs(x - y) < epsilon)  # This should print True as well
