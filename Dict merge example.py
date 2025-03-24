data1 = {1: 1, 2: 4}
data2 = {3: 6, 4: 16}
merged_data = {**data1, **data2}
merged_data[5] = 25  # Adding new key-value pair
print(merged_data)
