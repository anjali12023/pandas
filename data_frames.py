import pandas as pd

# DataFrame = tabular DS with rows and columns
#similar to excel spreadsheet

data = {"Name": ['Anjali', 'Aanchal', 'Navraj'], 
        "Age": [19, 21, 1]
}

#converting dictionary into data frame
df = pd.DataFrame(data, index = ["Employee 1", "Employee 2", "Employee 3"])

# print(df.loc["Employee 1"])
# print(df.iloc[0])

# add a new column
df["Job"] = ["Doctor", "Cook", "N/A"]

# add a new row -- create a new df and then concatenate
#for each new row, a new dictionary is required
new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Scientist"}], 
                       index = ["Employee 4"])

#concatenate to existing df
df = pd.concat([df, new_row])

print(df)