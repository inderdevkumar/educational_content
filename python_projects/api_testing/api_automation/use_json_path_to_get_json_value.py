import requests
import json
import jsonpath

url= "https://reqres.in/api/users?page=2"

response= requests.get(url)
# TO print response
print(response)

# To display content/body of resposne

response_content= json.loads(response.text)
#print(response_content)

def just_display_value_for_any_key():

    page_value= jsonpath.jsonpath(response_content, "page")  # It will get of items
    print(page_value)

def Get_first_name_from_every_data():

    value= jsonpath.jsonpath(response_content, "data")
    for i in range(5):
        fn= value[0][i]["first_name"]
        print(fn)
    print(value, fn)

Get_first_name_from_every_data()
