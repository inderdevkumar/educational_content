from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.by import By

class grocery:
   
    def check_amounts(self):
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("https://grocer.nz/")

        click_stores= driver.find_element(By.XPATH, "//a[@href='/stores']")
        click_stores.click()

        get_each_store_tab= driver.find_elements(By.XPATH, "//a[@href='#' and position() > 1]")
        for item in get_each_store_tab[2:4]:
            item.click()
            time.sleep(2)
            pageLength = driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
            match = False
            while (match == False):
                lastCount = pageLength
                time.sleep(1)
                pageLength = driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight;return pageLength;")
                if lastCount == pageLength:
                    match = True
            get_all_labels= driver.find_elements(By.XPATH, "//input[@type='checkbox']")
            for store in get_all_labels:
                store.click()
        driver.close()
cls_obj= grocery()
cls_obj.check_amounts()
