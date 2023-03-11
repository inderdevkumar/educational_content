from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.by import By
import glob
import os

class dummy_web_page:
   
    def download_3_files(self):
        
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("https://demo.imacros.net/Automate/Downloads")
        
        #maximize browser
        driver.maximize_window()
        time.sleep(3)
        
        all_download_link= driver.find_elements(By.XPATH, "(//a[contains(text(), 'Download')])[position()<4]")
        BASE_FILE_DIR= r"/home/inder/Downloads/*.zip"
        count= 0
        for item in all_download_link:
            count= count+1
            item.click()
            print(f"File number {count} Download Started.......")
            time.sleep(1)  

        while True:
            list_of_files = glob.glob(BASE_FILE_DIR)
            files_with_size = [ (file_path, os.stat(file_path).st_size)
                    for file_path in list_of_files ]
            print(list_of_files)
            print(files_with_size)
            
            if any(item[1] == 0 for item in files_with_size):
                continue
            else:
                driver.close()

cls_obj= dummy_web_page()
cls_obj.download_3_files()

