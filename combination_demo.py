import itertools

numbers = [4, 5, 6]
comb_length = 2
combinations = itertools.combinations(numbers, comb_length)

print(list(combinations))
