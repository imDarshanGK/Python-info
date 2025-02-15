import weakref

class A: 
    pass

obj = A()

wref = weakref.ref(obj)

print(wref() is obj)
