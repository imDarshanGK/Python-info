squares = [i**2 for i in range(10)]
cubes = [i**3 for i in range(10)]

# Generating a list of tuples with both squares and cubes
squares_and_cubes = [(i**2, i**3) for i in range(10)]

# Printing the results
print("Squares:", squares)
print("Cubes:", cubes)
print("Squares and Cubes (as tuples):", squares_and_cubes)
