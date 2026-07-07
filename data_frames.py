import pandas as pd

# DataFrame = tabular DS with rows and columns
#similar to excel spreadsheet

data = {"Name": ['Anjali', 'Aanchal', 'Navraj'], 
        "Age": [19, 21, 1]
}

#converting dictionary into data frame
df = pd.DataFrame(data)

print(df)