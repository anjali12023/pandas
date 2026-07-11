import pandas as pd 
df = pd.read_csv("data.csv")

#selection by column: 
# print(df["Name"].to_string())

#selection by columns:
print(df[["Name", "Height", "Weight"]].to_string())