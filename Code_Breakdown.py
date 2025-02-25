def myFun(**kwargs):
    if not kwargs:
        print("No arguments provided.")
    else:
        for key, value in kwargs.items():
            print(f"{key} == {value}")
    print("Total number of arguments:", len(kwargs))

# Call the function
myFun(a=1, b=2, c=3)
myFun()
