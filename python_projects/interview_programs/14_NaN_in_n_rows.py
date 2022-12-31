print("========== question 14 ===========")

import pandas as pd
import numpy as np

list_2d= [[5.1, 3.5, 1.4, 0.2, "setosa"],
        [4.9, 3.0, 1.4, 0.2, "setosa"],
        [4.7, 3.2, 1.3, 0.2, "setosa"],
        [4.6, 3.1, 1.5, 0.2, "setosa"],
        [5.0, 3.6, 1.4, 0.2, "setosa"]]

df= pd.DataFrame(list_2d, columns= ["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width", "Species"])

df_new = df  # Without this also , same result
n= int(input("Enter the n rows to be introduced with NaN: "))

df.loc[0:n-1, "Sepal.Width"] = np.nan
df.loc[0:n-1, "Petal.Length"] = np.nan
print(df)
print(df_new)


