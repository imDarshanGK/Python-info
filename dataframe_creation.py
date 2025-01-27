import pandas as pd 

data = {"P":[10, 20, 30], "Q":[5, 15, 25]}
df = pd.DataFrame(data)

print(df[">file_here>"])
