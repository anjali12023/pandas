import pandas as pd 

#data cleaning = process of fixing/ removing incorrect, incomplete/ irrelevant data 

df = pd.read_csv("data.csv")

#1. Drop irrelevant columns
# df = df.drop(columns=["Legendary", "No"])

#2. Handle missing data
df = df.dropna(subset=["Type2"]) #drop any rows that don't have data for Type 2

print(df.to_string())