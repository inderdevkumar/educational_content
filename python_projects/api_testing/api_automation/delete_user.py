import requests
import json
import jsonpath

url= "https://reqres.in/api/users/2"


#Use delete response
response= requests.delete(url)
# TO print response
print(response)

