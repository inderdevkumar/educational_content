# Python automation with selenium and web actions 

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import pickle

class web_action:
    def cookies(self):

        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        list_of_websites= ["https://www.glassdoor.com/", "https://www.w3schools.com/", "https://www.facebook.com/"]

        for item in list_of_websites:
            driver.get(item)
            pickle.dump(driver.get_cookies(), open("/home/inder/cookies/cookies.pkl", "wb"))

        cookies = pickle.load(open("/home/inder/cookies/cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)

obj= web_action()
obj.cookies()

