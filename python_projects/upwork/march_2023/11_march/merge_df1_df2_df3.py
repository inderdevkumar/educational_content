import pandas as pd
import os
os.getcwd()

folder = 'leetcode'

df1 = pd.DataFrame({
'Keyword': ['chemical executive recruiter', 'chemical executive recruiter', 'chemical executive recruiter'],
'Rank': ['>100', '>100', '>100'],
'URL': ['', '', ''],
'Location': ['Australia', 'Canada', 'Germany'],
'Volume': ['Chemical', 'Chemical', 'Chemical'],
'Tags': ['', '', ''],
'date_scraped': ['2/20/23', '2/20/23', '2/20/23']
})

date_scrapped_column= df1["date_scraped"]

df2 = pd.DataFrame({
'Keyword': ['chemical executive recruiter', 'chemical executive recruiter', 'chemical executive recruiter'],
'Rank': ['>100', '>100', '>100'],
'URL': ['', '', ''],
'Location': ['Australia', 'Canada', 'Germany'],
'Volume': ['Chemical', 'Chemical', 'Chemical'],
'Tags': ['', '', ''],
'date_scraped': ['1/15/23', '1/15/23', '1/15/23']
})

df3 = pd.DataFrame({
'Keyword': ['chemical executive recruiter', 'chemical executive recruiter', 'chemical executive recruiter'],
'Rank': ['>100', '>100', '>100'],
'URL': ['', '', ''],
'Location': ['Australia', 'Canada', 'Germany'],
'Volume': ['Chemical', 'Chemical', 'Chemical'],
'Tags': ['', '', ''],
'date_scraped': ['3/1/23', '3/1/23', '3/1/23']
})

merged_df = pd.concat([df1, df2, df3])

merged_df = merged_df.reset_index()

del merged_df["index"]

merged_df = merged_df.pivot(index=['Keyword', 'Location', 'URL', 'Volume', 'Tags'], columns='date_scraped', values='Rank')
merged_df = merged_df.reset_index()
merged_df.columns.name = None
merged_df = merged_df.rename(columns={'2/20/23': 'Rank_2/20/23', '1/15/23': 'Rank_1/15/23', '3/1/23': 'Rank_3/1/23'})
merged_df = merged_df.reindex(columns=["Keyword", "Rank_2/20/23", "Rank_1/15/23", "Rank_3/1/23", "URL", "Location", "Volume", "Tags"])
result = pd.concat([merged_df, date_scrapped_column], axis=1, join='inner')

print(result)
