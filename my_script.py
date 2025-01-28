from collections import Counter
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = Counter(data)
print(counter.most_common(1)[0][0])