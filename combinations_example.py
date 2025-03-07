import itertools

# Generate Combinations without Repetition
result = list(itertools.combinations([1, 2, 3], 2))
print(result)

# Generate Combinations with Repetition
result_with_replacement = list(itertools.combinations_with_replacement([1, 2, 3], 2))
print(result_with_replacement)
