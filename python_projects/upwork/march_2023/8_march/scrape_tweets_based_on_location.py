from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class twitter:

    def get_tweets_as_per_location(self):

        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("https://twitter.com/home")
        time.sleep(10)
        user_id= driver.find_element(By.XPATH, "//input[@autocomplete='username']")
        user_id.send_keys("your_email")
        
        click_next= driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]")
        click_next.click()
        
        
        time.sleep(5)
        user_pass= driver.find_element(By.XPATH, "//input[@autocomplete='current-password']")
        user_pass.send_keys("your_pass")
        
        time.sleep(2)
        login_btn= driver.find_element(By.XPATH, "//span[contains(text(), 'Log in')]")
        login_btn.click()
        
        time.sleep(30)
        search_text= driver.find_element(By.XPATH, "//input[@placeholder='Search Twitter']")
        search_text.send_keys("cricket")
        search_text.send_keys(Keys.ENTER)
        
        time.sleep(5)
        click_people_from_anyone= driver.find_element(By.XPATH, "(//input[@name='People'])[1]")
        click_people_from_anyone.click()
        
        time.sleep(5)
        click_location_near_you= driver.find_element(By.XPATH, "(//input[@name='Location'])[2]")
        click_location_near_you.click()

        tweets_latest= driver.find_element(By.XPATH, "//span[contains(text(), 'Latest')]")
        tweets_latest.click()
        time.sleep(5)

        all_tweets= driver.find_elements(By.XPATH, "//div[@aria-label='Timeline: Search timeline']/div/div")
        
        list_all_tweets= []
        for item in all_tweets:
            list_all_tweets.append(item.text)

        print(list_all_tweets, len(list_all_tweets))

        

        time.sleep(10)
        driver.close()

cls_obj= twitter()
cls_obj.get_tweets_as_per_location()

