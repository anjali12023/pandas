import pandas as pd 

#data cleaning = process of fixing/ removing incorrect, incomplete/ irrelevant data 

df = pd.read_csv("data.csv")

#1. Drop irrelevant columns
df = df.drop(columns=["Legendary"])
print(df)