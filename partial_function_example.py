from functools import partial

def multiply(x, y, z):
    return x * y * z

# Create a partial function where the first argument (x) is fixed to 10
multiply_by_ten = partial(multiply, 10)

# Now you can call multiply_by_ten with the remaining arguments
print(multiply_by_ten(2, 3))
