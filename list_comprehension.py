squares = []
for i in range(10):
    squares.append(i**2)  
print("Traditional approach:", squares)
squares_comprehension = [i**2 for i in range(10)]  
print("List comprehension approach:", squares_comprehension)
