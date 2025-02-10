def reverse_count(start):
    while start > 0:
        yield start + 2  # Adding 2 to the value before yielding
        start -= 1

gen_obj = reverse_count(5)
print(list(gen_obj))
