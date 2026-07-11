import pandas as pd 
# df = pd.read_csv("data.csv")

#selection by column: 
# print(df["Name"].to_string())

#selection by columns:
# print(df[["Name", "Height", "Weight"]].to_string())

#Selection by row:
# print(df.loc[0])

#selection by Name
df = pd.read_csv("data.csv", index_col = "Name")

print(df.loc["Pikachu", ["Height", "Weight"]])