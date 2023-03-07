
# importing the necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


# getting the webpage
page = requests.get('https://www.glassdoor.co.in/Reviews/index.htm?overall_rating_low=3.5&page=1&locId=2856202&locType=C&occ=Senior%20Software%20Engineer')

# creating the soup object
soup = BeautifulSoup(page.content, 'html.parser')

# finding the table
table = soup.find_all('div', class_='row d-flex flex-wrap') #//div[@id='Explore']/div[3]/div/div[4]/div[2]/

data = []
for row in table:
    value= [item.text for item in row]
    data.append(value)

print(data)
print(len(data))
# creating the dataframe
df = pd.DataFrame(data, columns=['company_name', 'salary', 'location', 'global_size', 'business', 'description'])

# saving the dataframe to excel
df.to_excel('glassdoor.xlsx', index=False)