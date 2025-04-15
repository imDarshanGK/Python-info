def fun(x):
    a = "Py"
    x = x ** 3
    combined = a + str(x)
    is_even = (x % 2 == 0)
    return combined, x, is_even

result = fun(4)
print(result)
