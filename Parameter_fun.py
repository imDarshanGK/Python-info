def func(x=1, y=2):
    if x > y:
        # Swap x and y
        x, y = y, x
    x = x + y
    y += 1
    print(x, y)

# Calling the function
func(y=2, x=1)  # Outputs: 3 3
func(x=3, y=1)  # Outputs: 4 2 (since x > y, it swaps)
