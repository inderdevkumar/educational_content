
# importing the necessary libraries

import pandas as pd
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.by import By


class drugs:

    def cost_n_drugs(self):

        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("https://costplusdrugs.com/")
        time.sleep(3)
        all_medication_button= driver.find_element(By.XPATH, "//div/button[@data-testid='browseAll-medications-button']")
        all_medication_button.click()
        
        time.sleep(2)
        all_medications_link= driver.find_element(By.XPATH, "//div/button[@data-testid='column_item_All']")
        all_medications_link.click()
        time.sleep(5)

        get_drug_details= driver.find_elements(By.XPATH, "//div[@role='rowgroup']/div")

        all_drug_list= []
        for i in range(len(get_drug_details)):
            drug_str= get_drug_details[i].text
            list1= drug_str.split("\n")
            all_drug_list.append(list1)
        
        df = pd.DataFrame(all_drug_list, columns =['Medication', 'Form','Retail Price', 'Our Price','Savings', 'Link'])

        df.to_csv("/home/inder/my_data/upwork_data/march_2023/medication.csv")
        

        driver.close()
cls_obj= drugs()
cls_obj.cost_n_drugs()
