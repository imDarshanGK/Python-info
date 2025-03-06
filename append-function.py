def func(x, y=[4, 2]):
    y.append(x)
    y.append('new')  # Adding 'new' to the list
    return y

print(func(1, [3, 2]))
