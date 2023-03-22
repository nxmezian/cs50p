import pandas as pd

df = pd.read_csv("testprofile.csv")

print(df.to_string(index=False))
