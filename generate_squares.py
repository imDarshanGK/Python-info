n = int(input("Enter a number: "))
squares = {x: x**2 for x in range(n)}
print(f"Squares from 0 to {n - 1}: {squares}")
