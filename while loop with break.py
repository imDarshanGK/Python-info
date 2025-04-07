i = 0
while i < 5:
    print(i, end=' ')
    i += 1
    if i == 3:
        print(" - Breaking the loop")
        break
    else:
        print(0, end=' ')
else:
    print("\nLoop completed without break.")
