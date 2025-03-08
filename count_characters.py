import collections

# Create a counter from a string
counter = collections.Counter("aabbccc")

# Get the two most common elements
print(counter.most_common(2))
