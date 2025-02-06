import pandas as pd

data = {"A": [1,2,3,4,5]}
df = pd.DataFrame(data)
df["B"] = df["A"] ** 2

print(df[(df["A"] > 1) & (df["B"] % 2 == 0)])
