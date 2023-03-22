import requests
import json
import jsonpath


url= "https://reqres.in/api/users"

with open("my_input_json.json", "r") as file:
    file_content= file.read()

json_file= json.loads(file_content)

response= requests.post(url, json_file)
print(response)

# NOw check the data u have put is same or not

into_json= json.loads(response.text)
response_value= jsonpath.jsonpath(into_json, "post")

print(response_value)
