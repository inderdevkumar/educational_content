from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

class linked_in:
   
    def get_people_tab_url(self):
        
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("https://www.linkedin.com/")
        
        #maximize browser
        driver.maximize_window()
        time.sleep(3)
        
        un= driver.find_element(By.XPATH, "//input[@autocomplete= 'username']")
        un.send_keys("id0102yadav@gmail.com")

        pw= driver.find_element(By.XPATH, "//input[@autocomplete= 'current-password']")
        pw.send_keys("Koderma@123#")

        click_sign_in= driver.find_element(By.XPATH, "//button[@type= 'submit']")
        click_sign_in.click()
        
        time.sleep(10)
        df = pd.read_excel("/home/inder/my_data/upwork_data/march_2023/11_march/forUpwork.xlsx", sheet_name= "PEOPLE", engine='openpyxl')
        
        all_url_list= []
        for index, row in df.iterrows():
            text_to_send= row["Name"]+" "+row["Company"]
            search_box= driver.find_element(By.XPATH, "(//input[@type= 'text'])[1]")
            search_box.send_keys(text_to_send)
            search_box.send_keys(Keys.ENTER)
            time.sleep(2)
            profile= driver.find_element(By.XPATH, "//span[text()= 'View full profile']")
            profile.click()
            time.sleep(3)
            all_url_list.append(driver.current_url)
        
        df["Linkedin URL2"]= all_url_list
        
        df.to_excel("/home/inder/my_data/upwork_data/march_2023/11_march/people_url.xlsx")
        time.sleep(5)
        driver.close()

cls_obj= linked_in()
cls_obj.get_people_tab_url()

