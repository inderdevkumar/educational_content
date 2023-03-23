from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.by import By

class facebook:
   
    def share_friends(self):

        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("https://www.facebook.com/")
        user_id= driver.find_element(By.NAME, "email")
        user_id.send_keys("your_gmail")

        user_pass= driver.find_element(By.NAME, "pass")
        user_pass.send_keys("your_password")

        login_btn= driver.find_element(By.NAME, "login")
        login_btn.click()
        time.sleep(10)
        option_share= driver.find_element(By.XPATH, "//div[@aria-label='Send this to friends or post it on your Timeline.']")
        option_share.click()
        time.sleep(5) 
        click_share_friend= driver.find_element(By.XPATH, "//span[contains(text(),'Share now (Friends)')]")
        click_share_friend.click()
        time.sleep(5)
        driver.close()

cls_obj= facebook()
cls_obj.share_friends()

