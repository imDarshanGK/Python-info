numbers = [1, 2, 3, 4, 5, 6]

# Filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Calculate the sum of even numbers
sum_of_even_numbers = sum(even_numbers)

# Print the even numbers and their sum
print(f"Even numbers: {even_numbers}")
print(f"Sum of even numbers: {sum_of_even_numbers}")
