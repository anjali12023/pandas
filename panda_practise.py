import pandas as pd

#series -- a 1D labelled array 

# data = [True, 102, 104, 200, 202]

# series = pd.Series(data, index=["a", "b", "c", "d", "e"])


# print(series[series < 200])

#create a python dict to record how many calories eaten a day
calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}

series = pd.Series(calories)
print(series)