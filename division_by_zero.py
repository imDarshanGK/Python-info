x = 10
try:
    print(x / 0)
except Exception as e:
    print(e)
    with open("log.txt", "a") as f:
        f.write(f"Error: {e}\n")
