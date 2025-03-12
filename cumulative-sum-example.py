a = [1, 2, 3, 4]
b = [sum(a[0:x+1]) for x in range(0, len(a))] 

# New feature: Calculate the differences between consecutive cumulative sums and elements in `a`
b_diff = [b[i] - b[i-1] if i > 0 else b[i] for i in range(len(b))]  # Difference between consecutive sums

print("Cumulative sum (b):", b)
print("Differences between consecutive cumulative sums (b_diff):", b_diff)