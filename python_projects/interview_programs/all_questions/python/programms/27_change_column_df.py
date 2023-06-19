print("========== question 27 ===========")

import pandas as pd


list_2d= [[5.1, 3.5, 1.4, 0.2, "setosa"],
        [4.9, 3.0, 1.4, 0.2, "setosa"],
        [4.7, 3.2, 1.3, 0.2, "setosa"],
        [4.6, 3.1, 1.5, 0.2, "setosa"],
        [5.0, 3.6, 1.4, 0.2, "setosa"]]

df= pd.DataFrame(list_2d, columns= ["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width", "Species"])
#df.columns = df.columns.str.replace('Sepal.Length', 'S_Length')

#  OR
df1= df.rename(columns= {"Sepal.Length": "S_Length"})
print(df1)
#print(filtered_df)
