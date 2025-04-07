def decimalToBinary(n):
    # Ensure input is an integer
    if isinstance(n, int):
        if n < 0:
            return "Input should be a non-negative integer."
        return "{0:b}".format(n)
    else:
        return "Input should be an integer."

# Example usage:
binary = decimalToBinary(23)
print(f"Binary of 23: {binary}")
