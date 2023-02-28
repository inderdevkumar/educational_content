from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class class_find_element_by_xpath:
   
    def locate_by_xpath(self):

        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("https://www.facebook.com/")
        user_id= driver.find_element(By.NAME, "email")
        user_id.send_keys("indra0102thetiger@gmail.com")

        user_pass= driver.find_element(By.NAME, "pass")
        user_pass.send_keys("kumar0102")

        login_btn= driver.find_element(By.NAME, "login")
        login_btn.click()

        time.sleep(3)
        # CLick friends
        click_friends= driver.find_element(By.XPATH, "//input[@type='search']")
        click_friends.send_keys("Himadri Tanaya")
        click_friends.send_keys(Keys.ENTER)
        time.sleep(8)

        # Click on message
        message_btn= driver.find_element(By.XPATH, "//span[contains(text(),'Message')]")
        message_btn.click()
        time.sleep(3)
        message_btn.send_keys("Hi")
        message_btn.send_keys(Keys.ENTER)
        driver.close()

cls_obj= class_find_element_by_xpath()
cls_obj.locate_by_xpath()
#browser.close()

