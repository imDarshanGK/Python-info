import itertools

numbers = [4, 5, 6]
comb_length = 2
permutations = itertools.permutations(numbers, comb_length)

print("Permutations:", list(permutations))
