from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#browser= webdriver.Firefox(executable_path= "/home/inder/my_data/doc/webdriver/geckodriver-v0.32.2-linux32/geckodriver")


driver.get("https://phoenixnap.com/kb/extract-tar-gz-files-linux-command-line")
print(driver.title)
#browser.close()

