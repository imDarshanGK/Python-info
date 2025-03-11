a = [1, 2, 3, 4]
b = [sum(a[0:x+1]) for x in range(0, len(a))]

for i, value in enumerate(b):
    print(f"Index {i}: Cumulative sum = {value}")
