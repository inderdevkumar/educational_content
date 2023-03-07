from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class class_find_element_by_xpath:
   
    def locate_by_xpath(self):

        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("https://www.facebook.com/")
        user_id= driver.find_element(By.NAME, "email")
        email= input("Enter email: ")
        passwd= input("Enter password: ")
        user_id.send_keys(email)

        user_pass= driver.find_element(By.NAME, "pass")
        user_pass.send_keys(passwd)

        login_btn= driver.find_element(By.NAME, "login")
        login_btn.click()

        time.sleep(3)
        # CLick friends
        list_of_friends= ["Himadri Tanaya", "Anubhav Kumar", "Anand Kumar Aky"]

        for item in list_of_friends:

            click_friends= driver.find_element(By.XPATH, "//input[@type='search']")
            click_friends.send_keys(item)
            click_friends.send_keys(Keys.ENTER)
            time.sleep(10)

        # Click on message
            message_btn= driver.find_element(By.XPATH, "//span[contains(text(),'Message')]")
            message_btn.click()
            time.sleep(3)
        
            content= f"Hi {item.split()[0]}, You are getting this message from automated script. Test is going on. Plz dont reply back, as I am not online:). Thanks!"
        # Write some message
            actions = ActionChains(driver)
            actions.send_keys(content)
            actions.send_keys(Keys.ENTER)
            actions.perform()
            time.sleep(3)

        driver.close()

cls_obj= class_find_element_by_xpath()
cls_obj.locate_by_xpath()
#browser.close()

