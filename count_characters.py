import collections

# Create a counter from a string
counter = collections.Counter("aabbccc")

# Get the two most common elements
print(counter.most_common(2))

# New feature: Count characters in a user-provided string and get the most common elements
user_string = input("Enter a string: ")
user_counter = collections.Counter(user_string)
most_common_elements = user_counter.most_common(2)
print(f"The two most common elements in the provided string are: {most_common_elements}")
