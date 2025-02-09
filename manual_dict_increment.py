d = {}

try:
    d["a"] += 1
except KeyError:
    d["a"] = 1

print(d["a"])
