import pandas as pd

main_df= pd.read_csv("all_data.txt", sep=" ")
print(main_df)

print(main_df.columns)
#Filter with multiple conditions with all columns
print(main_df[(main_df['date'] >= "26-09-2022") & (main_df['date'] <= "27-09-2022")])

modifiled_df_columns= main_df[["name", "amount"]]

#Filter with multiple conditions with all specific columns
filtered_dfspecific_columns= modifiled_df_columns[(main_df['date'] >= "26-09-2022") & (main_df['date'] <= "27-09-2022")]

filtered_dfspecific_columns.to_csv("filtered_dfspecific_columns_using_python.txt", sep=" ", index=False)

