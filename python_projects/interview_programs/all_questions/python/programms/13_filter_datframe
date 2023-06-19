print("========== question 13 ===========")

import pandas as pd


list_2d= [[5.1, 3.5, 1.4, 0.2, "setosa"],
        [4.9, 3.0, 1.4, 0.2, "setosa"],
        [4.7, 3.2, 1.3, 0.2, "setosa"],
        [4.6, 3.1, 1.5, 0.2, "setosa"],
        [5.0, 3.6, 1.4, 0.2, "setosa"]]

df= pd.DataFrame(list_2d, columns= ["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width", "Species"])

filtered_df= df[(df['Sepal.Length'] > 5) & (df['Sepal.Width'] > 3)]  # Here and is not working
print(df)
print(filtered_df)
