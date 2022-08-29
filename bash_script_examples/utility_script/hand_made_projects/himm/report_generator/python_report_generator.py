import pandas as pd

input_df= pd.read_excel("/home/inder/my_data/doc/task_to_do.xlsx")
print(input_df.head())

filter_hit_count_df= input_df[input_df["hit_count"] >= 25]
filter_hit_count_with_columns_df= filter_hit_count_df[["system_id", "date", "hit_count"]]

filter_no_hit_count_df= input_df[input_df["no_hit_count"] >= 25]
filter_no_hit_count_with_columns_df= filter_no_hit_count_df[["system_id", "date", "no_hit_count"]]

print("\n\n")
print(filter_hit_count_df.head())
print("\n\n")
print(filter_no_hit_count_df.head())
print("\n\n")

#Convert each df to txt file now
#df.to_csv(r'c:\data\pandas.txt', header=None, index=None, sep=' ', mode='a')

filter_hit_count_with_columns_df.to_excel("/home/inder/my_data/educational_content/bash_script_examples/utility_script/hand_made_projects/himm/report_generator/hit_count.xlsx")

#filter_hit_count_with_columns_df.to_csv("/home/inder/my_data/educational_content/bash_script_examples/utility_script/hand_made_projects/himm/report_generator/hit_count.txt", sep=' ', mode='a')

#filter_no_hit_count_with_columns_df.to_csv("/home/inder/my_data/educational_content/bash_script_examples/utility_script/hand_made_projects/himm/report_generator/no_hit_count.txt", sep=' ')

#filter_no_hit_count_with_columns_df.to_csv("/home/inder/my_data/educational_content/bash_script_examples/utility_script/hand_made_projects/himm/report_generator/hit_count.txt", sep=' ', mode='a')

#filter_no_hit_count_with_columns_df.to_csv("/home/inder/my_data/educational_content/bash_script_examples/utility_script/hand_made_projects/himm/report_generator/no_hit_count.txt", sep=' ')


print("--- done ---")
