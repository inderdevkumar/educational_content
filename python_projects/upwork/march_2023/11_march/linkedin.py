from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains

class linked_in:
   
    def get_people_tab_url(self):
        
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        #driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.linkedin.com/")
        
        #maximize browser
        driver.maximize_window()
        time.sleep(3)
        
        un= driver.find_element(By.XPATH, "//input[@autocomplete= 'username']")
        un.send_keys("your_email")

        pw= driver.find_element(By.XPATH, "//input[@autocomplete= 'current-password']")
        pw.send_keys("your_pass")

        click_sign_in= driver.find_element(By.XPATH, "//button[@type= 'submit']")
        click_sign_in.click()
        
        time.sleep(30)
        df = pd.read_excel("/home/inder/my_data/upwork_data/march_2023/11_march/forUpwork.xlsx", sheet_name= "PEOPLE", engine='openpyxl')
        
        all_url_list= []
        for index, row in df.iterrows():
            text_to_send= row["Name"]+" "+row["Company"]
            search_box= driver.find_element(By.XPATH, "(//input[@type= 'text'])[1]")

            search_box.send_keys(text_to_send)
            time.sleep(2)
            actions = ActionChains(driver)

            actions.send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
            time.sleep(3)
            #action.send_keys(Keys.ENTER)
            #action.perform()
            """
            all_searched_result= driver.find_elements(By.XPATH, "(//div[@role= 'option']/div)[position()<last()]")
            print(len(all_searched_result))
            for result in all_searched_result:
                print(row["Name"].lower(), row["Company"].lower())
                print(result.text.lower())
                if ((row["Name"].lower() in result.text.lower()) and (row["Company"].lower() in result.text.lower())):
                    result.click()
                    break
            """
            time.sleep(5)

            try:
                profile= driver.find_element(By.XPATH, "//span[text()= 'View full profile']")
                profile.click()
                time.sleep(3)
                all_url_list.append(driver.current_url)
            except:
                all_url_list.append("Profile not found")
        df["Linkedin URL2"]= all_url_list
        
        
        df.to_excel("/home/inder/my_data/upwork_data/march_2023/11_march/people_url.xlsx")
        time.sleep(5)
        print(df["Name"])
        driver.close()

cls_obj= linked_in()
cls_obj.get_people_tab_url()

