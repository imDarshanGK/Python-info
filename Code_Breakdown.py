def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
myFun(a=1, b=2, c=3)
#output
a == 1
b == 2
c == 3
