def fun(x):
    x += 1
    def innerfun():
        return y**3 + 1 
    return innerfun() + 5, x 

x, y = 5, 3
print(fun(x)) 
