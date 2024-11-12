x = 10
try:
    print(x / 0)  # This will raise a ZeroDivisionError
except Exception as e:
    print(e)  # This will catch the exception and print it
