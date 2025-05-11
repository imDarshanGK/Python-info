List = [1, 0, 2]

a, b, c = List[::-1]

if sum(List) % 2 == 0:
    print("The sum of the original list is even.")
else:
    print("The sum of the original list is odd.")

print(List[b])
