matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Sum of rows
row_sums = list(map(sum, matrix))

# Sum of columns
col_sums = [sum(col) for col in zip(*matrix)]

print("Sum of rows:", row_sums)
print("Sum of columns:", col_sums)