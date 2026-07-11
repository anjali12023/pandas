import pandas as pd 
#aggregate functions reduce a set of values into a single summary cvalue 
# used to summarise and analyse data (often used with groupby() function)

df = pd.read_csv("data.csv")

# WHOLE DATA FRAME 
#find the mean of any columns that are numeric 
# print(df.mean(numeric_only =True))
# print(df.sum(numeric_only =True))
# print(df.min(numeric_only =True))
# print(df.max(numeric_only =True))
# print(df.count()) #counting number of values within each column 

#SINGLE DATAFRAME
# print(df["Height"].mean())
# print(df["Height"].sum())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count()) #counting number of values within each column 

#GROUP BY()

group = df.groupby("Type1")

#group by Type 1, find mean of heights
# print(group["Height"].mean())

print(group["Height"].sum()) #ie all Bug types have combined height of 10.8
#other aggregate functions can be used as well 