# Import the required Module
import tabula
import pandas as pd

# Read a PDF File
#df = tabula.read_pdf("/home/inder/my_data/upwork_data/march_2023/visit_revenue.pdf", pages='all')[0]
# convert PDF into CSV
#df.to_excel("/home/inder/my_data/upwork_data/march_2023/visit_revenue.xlsx")

load_excel= pd.read_excel("/home/inder/my_data/upwork_data/march_2023/visit_revenue.xlsx", 
        engine='openpyxl', dtype='str')

df_new = load_excel.iloc[:, [1,3,4]]

df_new.rename(columns = {'Unnamed: 0.1': 'Search', 'Unnamed: 1': 'Visits'}, inplace = True)
print(df_new.head())

for index, row in df_new.iterrows():
   # print(index, row)
    if "Page" in row["Search"]:
        #print(index, row)
        print(df_new.iloc[index-1] + '\n' + df_new.iloc[index])
        #df_new= df_new.iloc[index-1] + '\n' + df_new.iloc[index]
        #df_new = df_new.iloc[index+1:].reset_index(drop=True)
        #df_new = df_new.apply(pd.to_numeric)

print(df_new.head())

