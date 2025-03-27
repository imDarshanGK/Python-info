nums = []
even_odd = []  # New list to store "even" or "odd"
cumulative_sum = 0  # Initialize the cumulative sum variable

for i in range(5):
    value = i + (True + (False / True))  # The original expression
    nums.append(value)
    even_odd.append("even" if value % 2 == 0 else "odd")  # Check if the value is even or odd
    cumulative_sum += value  # Add the current value to the cumulative sum

print(f"Final nums: {nums}")
print(f"Even/Odd: {even_odd}")
print(f"Final cumulative sum: {cumulative_sum}")
