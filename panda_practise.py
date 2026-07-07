import pandas as pd

#series -- a 1D labelled array 

data = [100, 102, 104]

series = pd.Series(data, index=["apartment 1", "apartment 2", 'apartment 3'])
print(series)
