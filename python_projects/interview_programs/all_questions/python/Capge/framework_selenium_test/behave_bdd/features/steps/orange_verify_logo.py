from behave import *
# or from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

@given(u'I launch chrome browser')
def launch_browser(context):
    context.driver= webdriver.Chrome(executable_path=ChromeDriverManager().install())
    # or context.driver= webdriver.Chrome(executable_path= path_for_chrome_driver)
    # or context.driver= webdriver.Chrome()  -> only if your chrome driver is stored in script folder of python
    # ie C:\Users\HIMADRI TANAYA\AppData\Local\Programs\Python\Python310\Scripts and add this path to env variable

@when(u'I open orange hrm homepage')
def open_orange_hrm_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    context.driver.maximize_window()


@then(u'I verify logo present in the home page')
def verify_logo(context):
    #context.driver.implicitly_wait(20)
    time.sleep(12)
    check_logo= context.driver.find_element(By.XPATH, "//img[@alt='company-branding']").is_displayed()

    print(check_logo)
    assert check_logo is True

@then(u'close the browser')
def close_browser(context):
    context.driver.close()
