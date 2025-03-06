def find_max_min(lst):
    if not lst:
        return "Empty list"
    return max(lst), min(lst), lst.index(max(lst)), lst.index(min(lst))

my_list = [3, 1, 4, 1, 5, 9, 2]
print(find_max_min(my_list))  # Output: (9, 1, 5, 1)
