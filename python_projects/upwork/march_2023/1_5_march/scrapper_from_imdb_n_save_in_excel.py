
# importing the necessary libraries

import pandas as pd
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.by import By


class imdb:

    def get_top5_movies_with_their_details(self):

        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("https://www.imdb.com/chart/top/")
        time.sleep(3)
        get_movies_link= driver.find_elements(By.XPATH, "//tbody[@class='lister-list']/tr[position()<6]/td[2]/a")
        movie_details= []
        movie_description= []
        movie_name= []

        for i in range(len(get_movies_link)):
            moview_select= driver.find_elements(By.XPATH, "//tbody[@class='lister-list']/tr[position()<6]/td[2]/a")
            movie_name.append(moview_select[i].text)
            moview_select[i].click()
            
            time.sleep(5)
            try:
                get_description= driver.find_element(By.XPATH, "//div[@data-testid= 'plot']/span[3]")
            except:
                get_description= driver.find_element(By.XPATH, "//p[@data-testid= 'plot']/span[3]")
            #get_description= driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/main[1]/div[1]/section[1]/section[1]/div[3]/section[1]/section[1]/div[3]/div[2]/div[1]/section[1]/p[1]/span[3]")
            movie_description.append(get_description.text)
            get_other_details= driver.find_elements(By.XPATH, "(//ul[@role='presentation'])[3]")
            for detail in get_other_details:
                 movie_details.append(detail.text)
            driver.back()
            time.sleep(2)

        #print(movie_name)
        #print(movie_details)
        driver.close()
        
        # modify_movie_details_list
        
        movie_details_list_v1= []
        for item in movie_details:
            list1= item.split("\n")
            movie_details_list_v1.append(list1)

        df1 = pd.DataFrame(movie_details_list_v1, columns =['Director1', 'Director','Writers1', 'Writers','Stars1', 'Stars'])
        df1_update= df1.drop(["Director1", "Writers1", "Stars1"], axis= 1)
        #print(df_update)
        #  Create df
        
        df = pd.DataFrame({'movies':movie_name,  'description':movie_description})
        #print (df)

        result = pd.concat([df, df1_update], axis=1, join='inner')
        #print(result)

        result.to_excel("imdb.xlsx")

cls_obj= imdb()
cls_obj.get_top5_movies_with_their_details()
