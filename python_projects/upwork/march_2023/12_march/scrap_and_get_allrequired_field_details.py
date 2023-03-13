from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

class webpage:

    def scrape_webpage(self):

        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.get("http://jefferson.softwaresystems.com/TICKET.html?TPTYR=2022&TPTICK=16080&TPSX=")
        time.sleep(4)
        tax_year= driver.find_element(By.XPATH,  "//div[@class='title']").text
        tax_year_list= tax_year.split(":")
        tax_year_input= [tax_year_list[0]]
        tax_year_output= [tax_year_list[1]]

        #print(tax_year_input, len(tax_year_input))
        #print(tax_year_output, len(tax_year_output))
        
        # FRom ticket number to Page
        table_pinfo_title= driver.find_elements(By.XPATH,  "(//table[@class='pinfo' ]//td[@class= 'title'])")

        table_pinfo_title_list= []
        for item in table_pinfo_title:
            table_pinfo_title_list.append(item.text)
        #print(table_pinfo_title_list, len(table_pinfo_title_list))

        table_pinfo_data= driver.find_elements(By.XPATH,  "(//table[@class='pinfo' ]//td[@class= 'data'])[position()<last()]")
        table_pinfo_data_list= []
        for item in table_pinfo_data:
            table_pinfo_data_list.append(item.text)

        get_index= table_pinfo_title_list.index("Property:")

        table_pinfo_data_list_modify1= table_pinfo_data_list[:get_index]+ ["".join(table_pinfo_data_list[get_index:get_index+4])]+ table_pinfo_data_list[get_index+4:]
        # 
        #print(table_pinfo_data_list_modify1, len(table_pinfo_data_list_modify1))
        
        

        # ====  FRom taxclass to Special Disposition: 	 =====================
        tr_valignb_first_input= driver.find_elements(By.XPATH,  "(//tr[@class='valignb'])[1]//td[position() mod 2 != 0]")
        tr_valignb_first_output= driver.find_elements(By.XPATH,  "(//tr[@class='valignb'])[1]//td[position() mod 2 = 0]")
        
        tr_valignb_first_input_list= []
        tr_valignb_first_output_list= []
        for i in range(len(tr_valignb_first_input)):
            tr_valignb_first_input_list.append(tr_valignb_first_input[i].text)
            tr_valignb_first_output_list.append(tr_valignb_first_output[i].text)

        #print(tr_valignb_first_input_list, len(tr_valignb_first_input_list))
        #print(tr_valignb_first_output_list, len(tr_valignb_first_output_list))
        

        # =========  From DUE: to Total Due ================
        tr_valignb_second_section= driver.find_element(By.XPATH,  "(//tr[@class='valignb'])[2]//td[position() =1]")
        tr_valignb_second_input= driver.find_elements(By.XPATH,  "(//tr[@class='valignb'])[2]//td[position() mod 2 = 0 and position()>1]")
        tr_valignb_second_output= driver.find_elements(By.XPATH,  "(//tr[@class='valignb'])[2]//td[position() mod 2 != 0 and position()>1]")

        tr_valignb_second_input_list= []
        tr_valignb_second_output_list= []
        for i in range(len(tr_valignb_second_input)):
            tr_valignb_second_input_list.append(tr_valignb_second_input[i].text)
            tr_valignb_second_output_list.append(tr_valignb_second_output[i].text)
        
        #print(tr_valignb_second_section.text)
        #print(tr_valignb_second_input_list, len(tr_valignb_second_input_list))
        #print(tr_valignb_second_output_list, len(tr_valignb_second_output_list))
        
        # ====================
        ptable_titleg= driver.find_elements(By.XPATH,  "//table[@class='ptable']//tr//td[@class= 'titleg']")
        ptable_title= driver.find_elements(By.XPATH,  "//table[@class='ptable']//tr//td[@class= 'title']")
        ptable_data= driver.find_elements(By.XPATH,  "//table[@class='ptable']//tr//td[@class= 'data']")
        ptable_pdata= driver.find_elements(By.XPATH,  "//table[@class='ptable']//tr//td[@class= 'pdata']")
        
        ptable_titleg_list= []
        ptable_title_list= []
        ptable_data_list= []
        ptable_pdata_list= []
        for item in ptable_titleg:
            ptable_titleg_list.append(item.text)

        for item in ptable_title:
            ptable_title_list.append(item.text)

        for item in ptable_data:
            ptable_data_list.append(item.text)

        for item in ptable_pdata:
            ptable_pdata_list.append(item.text)
        
        # MOdify into 1p column and output column
        input_column1_1= [ptable_title_list[i]+"_"+ptable_titleg_list[1] for i in range(3)]
        input_column1_2= [ptable_title_list[i]+"_"+ptable_titleg_list[2] for i in range(3)]
        input_column1_3= [ptable_title_list[i]+"_"+ptable_titleg_list[3] for i in range(3)]
        input_column1= input_column1_1 + input_column1_2 + input_column1_3

        input_column2_1= [ptable_title_list[i]+"_"+ptable_titleg_list[5] for i in range(3,8)]
        input_column2_2= [ptable_title_list[i]+"_"+ptable_titleg_list[6] for i in range(3,8)]
        input_column2= input_column2_1 + input_column2_2

        output_column1= [ptable_data_list[i] for i in range(len(ptable_data_list))]
        output_column2= [ptable_pdata_list[i] for i in range(len(ptable_pdata_list))]
        
        all_input= tax_year_input+ table_pinfo_title_list+ tr_valignb_first_input_list+ tr_valignb_second_input_list+input_column1 + input_column2
        all_output= tax_year_output+table_pinfo_data_list_modify1 + tr_valignb_first_output_list+tr_valignb_second_output_list+ output_column1+ output_column2
        print(all_input, len(all_input))
        get_index_More_Info= all_input.index("More Info:")

        get_more_info_link= driver.find_element(By.XPATH, "//a[contains(text(), 'Details')]")
        

        all_output[get_index_More_Info]= get_more_info_link.get_attribute("href")
        print(all_output, len(all_output))
        time.sleep(2)
        
        # dictionary of lists
        dict_use = {'Input': all_input, 'Output': all_output}

        df = pd.DataFrame(dict_use)
        print(df.head())
        df.to_excel("/home/inder/my_data/upwork_data/march_2023/11_march/scrapped.xlsx")
        driver.close()

cls_obj= webpage()
cls_obj.scrape_webpage()

