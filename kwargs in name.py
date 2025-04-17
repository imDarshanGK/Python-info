def func(name, **kwds):
    return kwds.get('name', name)

print(func(1, **{'name': 2})) 
print(func(1))                
