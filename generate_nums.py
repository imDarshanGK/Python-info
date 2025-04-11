nums = []
for i in range(5):
    val = i + (True + (False / True))  # still equals i + 1.0
    parity = "even" if int(val) % 2 == 0 else "odd"
    nums.append((val, parity))  # store as tuple: (number, "even"/"odd")

print(nums)
