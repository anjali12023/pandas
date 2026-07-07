import pandas as pd

#series -- a 1D labelled array 

data = [100, 102, 104]

series = pd.Series(data, index=["a", "b", "c"])

series.loc["c"] = 200
print(series)


#loc -- location by label 
#access loc property and change