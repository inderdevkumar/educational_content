from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

class class_find_element_by_id:
    def locate_by_id(self):

        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_id("login-input").send_keys("test@test.com")

cls_obj= class_find_element_by_id()
cls_obj.locate_by_id()
#browser.close()

