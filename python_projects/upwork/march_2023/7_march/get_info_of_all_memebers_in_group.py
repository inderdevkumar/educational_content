from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.by import By

class facebook:
    def backup(self):
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("https://www.facebook.com/groups/341868919278348/members")
        time.sleep(3)
        user_id= driver.find_element(By.NAME, "email")
        user_id.send_keys("indra0102thetiger@gmail.com")

        user_pass= driver.find_element(By.NAME, "pass")
        user_pass.send_keys("kumar0102")

        login_btn= driver.find_element(By.ID, "loginbutton")
        login_btn.click()
        time.sleep(10)
        friends_see_all= driver.find_element(By.XPATH, "(//div[contains(@class,'x6s0dn4 x78zum5 xl56j7k x1608yet xljgi0e x1e0frkt')])[51]")
        friends_see_all.click()

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
        time.sleep(4)
        driver.back()
        time.sleep(2) # (//span[contains(text(),'See All')])[1]
        common_friends_see_all= driver.find_element(By.XPATH, "(//span[contains(text(),'See All')])[1]")
        common_friends_see_all.click()
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
        time.sleep(4)
        driver.back()

        time.sleep(5)
        driver.close()

    def share_friends(self):

        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("https://www.facebook.com/groups/341868919278348/members")
        time.sleep(3)
        user_id= driver.find_element(By.NAME, "email")
        user_id.send_keys("indra0102thetiger@gmail.com")

        user_pass= driver.find_element(By.NAME, "pass")
        user_pass.send_keys("kumar0102")

        login_btn= driver.find_element(By.ID, "loginbutton")
        login_btn.click()
        
        count=0
        while count<1:
            try:
                time.sleep(10)
                friends_see_all= driver.find_element(By.XPATH, "(//span[contains(text(),'See All')])[1]")
                friends_see_all.click()
                time.sleep(4)
                driver.back()
                count= count+1

            except:
                count= count+1
                print(f"{count} Exception")
        
        time.sleep(10)
        all_members= driver.find_elements(By.XPATH, "//div[@class='x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x2lah0s x193iq5w x1gslohp x12nagc xzboxd6 x14l7nz5']//span[contains(@class,'xt0psk2')]/a[@tabindex='0']")
        all_members[1].click()
        
        time.sleep(2)
        # Task 2:  Get memeber ID from URL
        url= driver.current_url
        print(url)
        
        # Task 3: Get info like city and contact
        member= driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]")
        member.click()

        time.sleep(2)
        select_main_profile= driver.find_element(By.XPATH, "//span[normalize-space()='View Main Profile']")
        select_main_profile.click()
        
        time.sleep(3)
        select_about= driver.find_element(By.XPATH, "//span[normalize-space()='About']")
        select_about.click()
        
        time.sleep(2)

        lives_in= driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[1]/span").text
        print(lives_in)

        from_place= driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[2]/div[1]/span").text
        print(from_place)
        
        click_contact= driver.find_element(By.XPATH, "//span[normalize-space()='Contact and basic info']")
        click_contact.click()
        time.sleep(2)

        contact_info= driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div").text
        print(contact_info)
        """
        members_list= []
        for item in all_members:
            members_list.append(item.text)
        print(members_list, len(members_list))
        """
        time.sleep(5)
        driver.close()

cls_obj= facebook()
cls_obj.share_friends()

