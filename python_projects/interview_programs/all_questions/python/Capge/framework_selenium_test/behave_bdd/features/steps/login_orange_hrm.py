from behave import *
# or from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

@when(u'Enter un "{user}" and pass "{pwd}"')
def enter_user_pass(context, user, pwd):
    time.sleep(10)
    user_name= context.driver.find_element(By.XPATH, "//input[@name='username']")
    user_name.send_keys(user)

    pass_wd= context.driver.find_element(By.XPATH, "//input[@name='password']")
    pass_wd.send_keys(pwd)


@when(u'click on login button')
def click_login(context):
    time.sleep(1)
    login= context.driver.find_element(By.XPATH, "//button[@type='submit']")
    login.click()


@when(u'click on User profile')
def click_profile(context):
    time.sleep(5)
    try:
        profile = context.driver.find_element(By.XPATH, "(//img[@alt='profile picture'])[1]")
        profile.click()
    except:
        context.driver.close()
        assert False, "Test Failed"


@when(u'click on About')
def click_about(context):
    time.sleep(3)

    try:
        all_dropdown = context.driver.find_elements(By.XPATH, "//li/ul//li")

        for item in all_dropdown:
            if item.text == "About":
                print("about")
                item.click()
                break

    except:
        context.driver.close()
        assert False, "Test Failed"

@then(u'verify if user is sucesffuly logged in and employee number greater than 25')
def verify_dashboard_n_employee(context):
    time.sleep(2)

    try:
        about_content= context.driver.find_elements(By.XPATH, "//div[@role='document']//div")
        text_content= [item.text for item in about_content]
        print("about content: ", int(text_content[7]))
        dashboard = context.driver.find_element(By.XPATH, "//h6")

    except:
        context.drive.close()
        assert False, "Test Failed"

    if ( dashboard.text == "Dashboard" and int(text_content[7]) > 25):
        assert True, "Test Passed"
