a = [1, 2]
b = [3, 4]

zipped_once = zip(a, b)
zipped_twice = zip(*zipped_once)

print(list(zipped_twice))
