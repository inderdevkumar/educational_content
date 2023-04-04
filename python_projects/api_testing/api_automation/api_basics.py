import requests

# 1st way ====================
url1= "https://reqres.in/api/users?page=2"
response1= requests.get(url1)

# 2nd way =====================

p= {"pages": 2}
url= "https://reqres.in/api/users"
response= requests.get(url, params= p)


print(response)  # <Response [200]>

code= response.status_code

print(code) # 200


# VVI ============
# print(dir(response))  # list of properties we have insuiide this response variables

"""
['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url']

"""


print(response.url) # To print url
#print(response.text)  # get content of response in unicode/ plain string

# print(response.json()) # It will return data in form of json

#print(response.content) #IT will reqtuen the content in byte format


json_res= response.json()  # WE will use json
print(json_res)
print(json_res["total"])

# GEt email for id= 7

# Method 1 without json path ====================
for i in range(len(json_res["data"])):

    if json_res["data"][i]["id"]== 7:
        print(json_res["data"][i]["email"])


#  post =================

def post_me():


    url= "https://reqres.in/api/users"

    dict_data= {"name": "Inder", "job": "Eng"} 

    res= requests.post(url, dict_data)

    print(res.status_code)

    print(res.json())

post_me()
