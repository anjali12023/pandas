import pandas as pd

#series -- a 1D labelled array 

data = [100, 102, 104, 200, 202]

series = pd.Series(data, index=["a", "b", "c", "d", "e"])


print(series[series >= 200])
#filter by values within the series with condition