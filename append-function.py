def func(x, y=[4, 2]):
    y.append(x)
    return y
print(func(1, [3, 2]))
