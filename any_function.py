my_list = [[], {}, (), "", 0]
truthy_elements = [item for item in my_list if item]  # Filter truthy values
print(f"Truthy elements: {truthy_elements}")
print(any(my_list))  # Checking if any element is truthy
