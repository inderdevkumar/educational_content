print("========== question 15 ===========")

import pandas as pd
import numpy as np


list_2d= [[1, np.nan, np.nan, np.nan],
        [2, 22.7, 1.0, 187.0],
        [1, np.nan, 1.0, 187],
        [3, np.nan, np.nan, np.nan],
        [1, 20.4, 1.0, 113.0]]

df= pd.DataFrame(list_2d, columns= ["age", "bmi", "hyp", "ch1"])
print(df)

age_nan_count= df['age'].isna().sum()
bmi_nan_count= df['bmi'].isna().sum()
hyp_nan_count= df['hyp'].isna().sum()
ch1_nan_count= df['ch1'].isna().sum()
print("Total NaN in age columns is: ", age_nan_count)
print("Total NaN in bmi columns is: ", bmi_nan_count)
print("Total NaN in hyp columns is: ", hyp_nan_count)
print("Total NaN in ch1 columns is: ", ch1_nan_count)

# or

print("Alternative method")
nan_values_in_df_detail= df.isna().sum()
print(nan_values_in_df_detail)
